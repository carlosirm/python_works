"""7-1. Rental Car: Write a program that asks the user what kind of rental car they
would like. Print a message about that car, such as “Let me see if I can find you
a Subaru.”"""

car = input ("What kind of car do you like to rent? ")
print ("Let me see if ther's a " + car + " available")


"""7-2. Restaurant Seating: Write a program that asks the user how many people
are in their dinner group. If the answer is more than eight, print a message saying
they’ll have to wait for a table. Otherwise, report that their table is ready."""

tablesize = input ("Welcome! How many are in your party?")
tablesize = int(tablesize)

if tablesize <= 8:
	print ("Yes, come by here please")
else:
	print ("Oh, can you please wait in the bar for an available table")

"""7-3. Multiples of Ten: Ask the user for a number, and then report whether 
the number is a multiple of 10 or not."""

number = input("Let´s see if your number is 10´s multiple")
number = int(number)

if number % 10 == 0:
	print ("Yes, your number " + str(number) + " is 10´s multiple ")
else:
	print ("Your number it's not 10´s multiple")

