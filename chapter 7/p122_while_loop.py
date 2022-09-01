print ("While loop")
current_number = 1
while current_number <= 5:
	print(f"El numero es {current_number}")
	current_number += 1


print ("*** Loop while users enters QUIT ***")
prompt =  "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program "

message = ""
while message != 'quit':
	message = input(prompt)
	print (message)


# Using a flag.
print ("*** Using a flag ***")
active = True
while active:
	message = input(prompt)
	if message == 'quit':
		active = False
		print ("El programa ha finalizado, chao chao")
	else:
		print(message)


print ("*** \nCities.py Using break ***")

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
	city = input(prompt)
	if city == 'quit':
		break
	else:
		print("I'd love to go to " + city.title() + "!")



print ("*** Using continue ***")

current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue
	print(current_number)