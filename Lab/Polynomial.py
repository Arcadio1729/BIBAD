import numpy as np

class Polynomial:
    def __init__(self,coefficients):
        self.coefficients=coefficients

    def __add__(self, other):
        deg=0
        if len(self.coefficients)>len(other.coefficients):
            deg=len(self.coefficients)
            other.coefficients.resize((deg,),refcheck=False)
        else:
            deg=len(other.coefficients)
            self.coefficients.resize((deg,),refcheck=False)

        #self.coefficients+=other.coefficients
        return Polynomial(self.coefficients+other.coefficients)

    def __sub__(self, other):
        deg=0
        if len(self.coefficients)>len(other.coefficients):
            deg=len(self.coefficients)
            other.coefficients.resize((deg,),refcheck=False)
        else:
            deg=len(other.coefficients)
            self.coefficients.resize((deg,),refcheck=False)

        #self.coefficients+=other.coefficients
        return Polynomial(self.coefficients-self.other)

    def __mul__(self,other):
        deg=0
        if len(self.coefficients)>len(other.coefficients):
            deg=len(self.coefficients)
            other.coefficients.resize((deg,),refcheck=False)
        else:
            deg=len(other.coefficients)
            self.coefficients.resize((deg,),refcheck=False)

        coef1=self.coefficients
        coef1.resize(len(self.coefficients),1)

        coef2=other.coefficients

        mulcoefsMatrix=coef1*coef2
        mulcoefs=calculateDiagonals(mulcoefsMatrix)

        return Polynomial(mulcoefs)

    def __str__(self):
        deg=0
        outstr=""
        for c in self.coefficients:
            outstr=outstr+(str(c)+"*x^"+str(deg)+"+")
            deg=deg+1
        return  outstr

    def getValue(self,x_val):
        s=0
        deg=0
        for c in self.coefficients:
            s=s+c*(x_val**deg)
            deg+=1

        return s

def calculateDiagonal(arr, rowNr, colNr):
    sums = []
    tempSum = 0

    if rowNr < (len(arr) - 1):
        for i in range(0, rowNr + 1):
            tempSum = tempSum + arr[rowNr - i, colNr + i]
    else:
        for i in range(colNr, len(arr)):
            tempSum = tempSum + arr[rowNr, i]
            rowNr -= 1
    return tempSum


def calculateDiagonals(arr):
    diagonals = []

    for i in range(len(arr) - 1):
        diagonals.append(calculateDiagonal(arr, i, 0))

    for i in range(len(arr)):
        diagonals.append(calculateDiagonal(arr, len(arr) - 1, i))

    return diagonals