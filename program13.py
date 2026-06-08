"""
Write a Python Program TO Check Leap Year .


# Divided By 100  means century year (ending with 00)

# century year divided by 400 is leap year 



# not divided by  100 means not a leap year 
# year Divided by 4 is a leep year 


# if not divided by both 400 (century year ) and 4 (not century year )
# year is not leep year 
"""

Year = int(input("Enter a Leep Year  :"))

if (Year%400==0) and (Year%100==0):
    print("{0} is a Leep year ".format(Year))

elif (Year%4==0) and (Year!=100):
    print("{0} is a Leep year ".format(Year))

else :
    print("{0} is not  a Leep year ".format(Year))

