from ExceptionTypes import  OnePointException
def find_line_equations(x1,y1,x2,y2):
    try:
        x1=float(x1)
        x2=float(x2)
        y1=float(y1)
        y2=float(y2)
        if x1==x2 and y1==y2:
            raise OnePointException("Cannot create two different points of these coordinates.")
        elif x1==x2:
            A=1
            B=0
            C=(-x1)
        elif y1==y2:
            A=0
            B=1
            C=(-y1)
        else:
            a=((y1-y2)/(x1-x2))
            b=(y1-(y1-y2)*x1/(x1-x2))
            A=a
            B=-1
            C=b
        return A,B,C
    except Exception as e:
        raise e