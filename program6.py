# write a python program to convert kilometers to miles.

kilometers=float(input("Enter Distance in kilometers : "))

#conversion factors : 1 kilometers = 0.621371 miles

conversion_factors=0.621371

miles=kilometers*conversion_factors

print(f"{kilometers} kilometers is equal to {miles} miles")

#end