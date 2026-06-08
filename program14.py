"""
Write a Python program to Check Prime Number .

Prime Number:

A prime number is a Whole a Number That cannot be enenly
Divided By any Other Number Except for 1 and itself.
For Example ,2,3,5,7,9,11,13,15 are 17 a  prime NUmbers Beacause They 
Cannot be any other Positive Integer except for 1 their own value .



"""

num = int(input("Enter a Number : "))

#Define a Flag Veriables 

flag=False

if num == 1:
    print(f"{num},this not a prime nummber ")
elif num > 1:
    
    for i in range(2,num):
        if (num% i)==0 :
            flag = True  # if factor is not found set a flag to true 
            # Break out of loop
            break
        # check if flag is True 

if flag :
    print(f"{num} is not a prime number ")
        
else :
    print(f"{num},is a prime number")



