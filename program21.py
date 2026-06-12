"""
Write a Python program to Find the sum of Natural Numbers .


Natural numbers are a set of positive integers that are used to count and order objects .
they are the numbers that typically start 1 and continue indefinitely, including all the 
whole numbers greater that 0 , in mathemathical notation, the set of natural numbers is often
denoted as "N" and can be axpressed as :
                       N = 1,2,3,4,5,6,7,8




"""
limit=int(input("Enter the limit: "))

# Initialize the Sum

sum=0

#Use a for Loop to calculate the sum of the natural numbers

for i in range(1,limit+1):
    sum +=i

print("The sum of Natural numbers up to ",limit,"is :",sum)

