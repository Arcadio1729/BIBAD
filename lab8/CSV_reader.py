#jako etykietę moduł przyjmuje numer kolumny będącej etykietą


import csv
import numpy as np

class CSV_reader:

    def __init__(self, file_path, label_column_nr,delimiter):
        self.file_path = file_path
        self.working_data = []
        self.delimiter = delimiter
        self.label_column_nr=label_column_nr



    def read_csv(self):
        with open(self.file_path) as csvDataFile:
            csvReader = csv.reader(csvDataFile, delimiter=self.delimiter)
            for row in csvReader:
                self.working_data.append(row)
            self.working_data = np.array(self.working_data)
            self.working_data = self.working_data.astype(np.float)
        csvDataFile.close()

    def standardize_data_column(self, column_nr):
        if column_nr!=self.label_column_nr:
            self.working_data[:, column_nr] = (self.working_data[:, column_nr] - self.working_data[:,column_nr].mean()) / self.working_data[:,column_nr].std()

    def center_data_column(self, column_nr):
        if column_nr != self.label_column_nr:
            self.working_data[:, column_nr] = self.working_data[:, column_nr] - self.working_data[:, column_nr].mean()

    def standardize_data(self):
        for i in range(self.working_data.shape[1]):
            self.standardize_data_column(i)

    def center_data(self):
        for i in range(self.working_data.shape[1]):
            self.center_data_column(i)


    def get_label(self):
        return self.working_data[:,self.label_column_nr]

    def get_data(self):
        selector = [col_nr for col_nr in range(self.working_data.shape[1]) if col_nr != self.label_column_nr]
        return self.working_data[:,selector]
