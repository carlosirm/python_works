"""7-8. Deli: Make a list called sandwich_orders and fill it with the names of various
sandwiches. Then make an empty list called finished_sandwiches. Loop
through the list of sandwich orders and print a message for each order, such
as I made your tuna sandwich. As each sandwich is made, move it to the list
of finished sandwiches. After all the sandwiches have been made, print a
message listing each sandwich that was made."""

print ("*** Deli.py ****")
sandwich_order = ['atun','pastrami','albondigas','J&Q','pastrami','vegeta','4quesos','pastrami']
finished_sandwiches = []

while  sandwich_order:
	current_sandwich = sandwich_order.pop()
	print (f"Preparando sandwich: {current_sandwich.title()}.")
	finished_sandwiches.append(current_sandwich)

print ("\nLista final de sandwich preparados")
for sandwich_name in finished_sandwiches:
	print (f"{sandwich_name.title()}")

"""7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches."""

print ("*** No pastrami.py ****")

flag = True

while flag:
	print
	if 'pastrami' in finished_sandwiches:
		finished_sandwiches.remove('pastrami')

	else:
		flag = False
		print ("pastrami sandwches are ran out")


print ("\nLista final de sandwich preparados")
for sandwich_name in finished_sandwiches:
	print (f"{sandwich_name.title()}")

"""7-10. Dream Vacation: Write a program that polls users about their dream
vacation. Write a prompt similar to If you could visit one place in the world,
where would you go? Include a block of code that prints the results of the poll."""

dream_vacation = {}

flag = True
while flag:
	name = input("Hi there! Whats your name?: ")
	place = input ("If you could go visit one place in the world, where would you go?: ")

	dream_vacation[name]=place
	terminar = input ("Te gustaria terminar la encuesta? Por favor Escribe 'quit': ")
	if terminar == 'quit':
		flag = False

print ("\nResultados de la encuesta")
for name, place in dream_vacation.items():
	print (f"{name.title()} tu lugar favorito para visitar es {place.title()} ")

