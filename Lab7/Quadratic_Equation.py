import math
from ExceptionTypes import NonRealException,NotQuadraticEquation
def solve_quadratic_equation(a,b,c):
    try:
        a=float(a)
        b=float(b)
        c=float(c)
        delta=b**2-4*a*c
        if a==float(0):
            raise NotQuadraticEquation("Cannot create quadratic equation from following coefficients: "+str(a)+","+str(b)+","+str(c)+".")
        elif delta<0:
            raise NonRealException("The quadratic equation does not have any solutions in real numbers.")
        else:
            x1=float((-b+math.sqrt(delta))/(2*a))
            x2=float((-b-math.sqrt(delta))/(2*a))
        if x1==x2:
            return x1
        else:
            return x1, x2
    except Exception as e:
        raise e