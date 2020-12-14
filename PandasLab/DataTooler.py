import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class DataTooler:
    def __init__(self,source1_path,source2_path):
        self.source1_path=source1_path
        self.source2_path=source2_path
        self.df1=pd.read_csv(source1_path)
        self.df2=pd.read_csv(source2_path)
        self.df=self.df1.append(self.df2)


    def remove_nan(self):
        for column in self.df:
            self.filtered_df = self.df[~self.df[column].isnull()]

    def convert_column_to_datetime(self,column_name):
        self.df[column_name]=pd.to_datetime(self.df[column_name])

    def plot_generator(self,start_day,end_day,source_key):
        new_df=self.df[(self.df['DATE_TIME'] <= end_day) & (self.df['DATE_TIME'] >= start_day) & (self.df['SOURCE_KEY'] == source_key)]
        new_df=new_df.set_index('DATE_TIME')
        AC_POWERS=new_df['AC_POWER'].resample('D').max()
        AC_POWERS.plot()

    def find_below(self, part_of_average):
        generators_mean = {}
        for sk in self.df['SOURCE_KEY'].unique():
            sk_df = self.df[self.df['SOURCE_KEY'] == sk]
            generators_mean[sk] = sk_df['AC_POWER'].mean()

        possible_defects = []
        total_mean = self.df['AC_POWER'].mean()
        for gk, gv in generators_mean.items():
            if gv < part_of_average * total_mean:
                possible_defects.append(gk)

        return possible_defects