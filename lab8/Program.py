from CSV_reader import CSV_reader
from Perceptron import Perceptron
import numpy as np

if __name__ == "__main__":
    c=CSV_reader("C:\\Users\\arcad\Desktop\\ja\\college\\IT\\BibliotekiAnalizyDanych\\sample1.csv",8,";")
    c.read_csv()
    c.standardize_data()
    y=c.get_label()
    X=c.get_data()
    w=np.zeros(X.shape[1])

    P=Perceptron(0.01,X,y,w,100)
    P.train()

    print(P.weights)