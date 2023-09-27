#!python3

#"""
#Write a program to ask the user to input a length in centimeters. Convert this into feet and inches.  Round your inches to the nearest whole inch.
#You will likely need to make use of at least one of the following:
#* % modulus
#* math.floor()

#Sample output:
#```
#Enter a length in centimeters: 172
#172 centimeters is 5 feet and 8 inches

#Enter a length in centimeters: 32
#32 centimeters is 1 feet and 1 inches
#```
#"""
print("Today I will convert a length in centimeters into feet and inches.")
lengthcm = int(input("Enter a length in centimeters-->"))
inch = lengthcm/2.54
inch = int(round(inch,0))
print(inch)
feet = int((inch - (inch % 12)) / 12)
print(feet)
inch = int(inch - feet * 12)
print(inch)
print(f"{lengthcm} centimeters is {feet} feet and {inch} inches.")