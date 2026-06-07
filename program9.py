# write a python program to solve quadratic equation.

"""
The standard form of a quadratic equation is :

                                              ax2+bx+c=0

                                              
where 

a.b and c are real numbers and 

a!=0

The Solutions of this quadratic equation is given by :
                                                     (-b+(or)-(b2-4ac)1/2)/(2a)



"""

import math


#Input coefficients 

a = float(input("Enter Coefficient a : "))
b = float(input("Enter Coefficient b : "))
c = float(input("Enter Coefficient c : "))

# Calculate the Discriminant 
discriminant = b**2 - 4*a*c

#Check if the Discriminant is positive,negative,or zero

#END


