"""
Write a Python program to print all prime Numbers in an Intervel of 1 -10

"""

lower = 1
upper=10

print("Prime Numbers between ",lower,"and",upper,"are :")

for num in  range(lower,upper+1):    # for loop  (1, 1+1):


    if num >1 :        # 1+1=2
        for i in range(2,num): #2 , 2
            if num % i==0 : 
                break
            
        else :
                print(num)



