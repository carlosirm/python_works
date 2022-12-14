"""7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza."""

prompt = "Hola! que toppings deseas agregarle a tu pizza"
prompt += "\nIngresa 'quit' para terminar tu solicitud: "


while True:
	pizza_topping = input(prompt)
	
	if pizza_topping == 'quit':
		print ("Gracias por comprar en pizza planeta, chao chao")
		break
	else:
		print (f"Genial, agregaremos {pizza_topping} a tu pizza")

		

"""7-5. Movie Tickets: A movie theater charges different ticket prices depending on 
a person’s age. If a person is under the age of 3, the ticket is free; if they are 
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. 
Write a loop in which you ask users their age, and then tell them the cost of their 
movie ticket."""

prompt = "Bienvenido a Cines Plaza"
prompt += "\nPor favor introduce tu edad y te informaremos el precio del ticket"

edad = input (prompt) 
edad = int(edad)
if edad <= 3:
	print (f"Your ticket it's free, please go ahead.")
elif edad <= 12:
	print (f"Your ticket cost it's $10, please go ahead.")
else:
	print (f"Your ticket cost it is $15")

"""7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
that do each of the following at least once:
• Use a conditional test in the while statement to stop the loop.
• Use an active variable to control how long the loop runs.
• Use a break statement to exit the loop when the user enters a 'quit' value."""

prompt = "Bienvenido a Cines Plaza"
prompt += "\nPor favor introduce tu edad y te informaremos el precio del ticket"

while True:
	edad = input (prompt) 

	if str(edad) == 'quit':
		break
	elif int(edad) <= 3:
		print (f"Your ticket it's free, please go ahead.")
	elif int(edad) <= 12:
		print (f"Your ticket cost it's $10, please go ahead.")
	else:
		print (f"Your ticket cost it is $15")

print ("programa finalizado")