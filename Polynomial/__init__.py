from Polynomial import Polynomial
from Student import Student
from Employee import  Employee
from Profesor import  Profesor
from  Teacher import  Teacher

import numpy as np

if __name__ == "__main__":
    s=Student("Hugo","Steinhaus","H@AGH.pl","1234")
    p=Profesor("Isaac","Newton","c@en.com","223")
    t=Teacher("Gotfried","Leibniz","g@de.com","997")

    t.sendEmail("Sir, my name is"+s.lastname+"Tell me please what's my grade.")
    s.addGrade("Algebra",3)
    s.sendEmail("Congratulations, your grade is 3. Regards"+t.lastname)
    print(s.inbox)
    print(t.inbox)
