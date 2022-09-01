# Store information about a pizza being ordered.
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
	'dressings':['Aceite de Oliva','Sal','Pimienta','Salsa de Cebollas']}
# Summarize the order.

print("You ordered a " + pizza['crust'] + "-crust pizza " +"with the following toppings:")

for topping in pizza['toppings']:
	print("\t" + topping)

print ('Y de Aderezos:')
for aderezo in pizza['dressings']:
	print ('\t' + aderezo )

# otra manera de resolverla.

print ('for your pizza you ordered: '  )
for clave, valor in pizza.items():
	print (clave + str(len(list(valor)) ))
	if len(valor) == 0:
		print (valor)
	else:
		for adicionales in valor:
			print (adicionales)