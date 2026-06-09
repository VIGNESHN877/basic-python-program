"""
Write a Python Program to Display the Multiplcation Table .
"""

num = int(input("Enter Multiplication table of : "))

for i in range(1,11):   # i in the range od the starting value and ending value 
    print(f"{i}*{num}={num*i}")  # input value * i of the loop = num*i = value print 
    