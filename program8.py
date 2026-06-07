import calendar

#  Write  a Python Program TO Display Calendar.


year = int(input("Enter Year :"))
month=int(input("Enter month : "))

cal=calendar.month(year,month)

print(cal)

#end