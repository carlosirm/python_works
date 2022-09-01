age = input ("How old are you? ")
age = int(age)
age >= 18


print ('Casting to int()')
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
	print("\nYou're tall enough to ride!")
else:
	print("\nYou'll be able to ride when you're a little older.")


print ('Exercise_ Even or odd')

number = input("Enter a number, and I'll tell you if its even or odd: ")
number = int(number)

if number % 2 == 0:
	print("\nThe number " + str(number) + " is even.")
else:
	print("\nThe number " + str(number) + " is odd.")


