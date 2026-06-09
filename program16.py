"""
Write a python program to  find the Factorial of a Number.

"""

num=int(input("Enter a Number : "))

factorial=1

if num < 0 :
    print("factorial does not exist for Negative Numbers ")

elif num == 0 :
    print("Factorial of 0 is 1 ")

else :
    for i in range(1,num+1):
        factorial = factorial*i
print(f"The factorial of {num} is {factorial}")