"""
Write a python program to find Armstrong Number in an Interval




"""


# input the interval from the user 

lower = int(input("Enter the lowest limit of the interval Number : "))
upper= int(input("Enter the upper limit of the interval Number : "))

for num in range(lower,upper+1):
    order=len(str(num)) # find the number of a digits in "num"
    temp_num=num
    sum=0

    while temp_num>0:
        digit=temp_num % 10
        sum +=digit ** order
        temp_num //=10

    # Check if "num" is an Armstrong number 

    if num == sum :
        print(num)

