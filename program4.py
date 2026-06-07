#write a python to swap two variables.

# Input Two Vvariables

a=input("Enter the Value of the frist variable (a):")
b=input("Enter the  Value of The Second variable (b):")

#Display the original values

print("Original values : a=",a,"b=",b)
#swap the values using a  temporary variable

temp=a
a=b
b=temp

# Display the swapped values 

print(f"Swapped Values : a = {a},b={b}")