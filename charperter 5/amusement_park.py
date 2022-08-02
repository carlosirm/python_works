# if elif else

# a. Admission for anyone under age 4 is free.
# b. Admission for anyone between the ages of 4 and 18 is $5.
# c. Admission for anyone age 18 or older is $10.

age = 3
if age < 4:
	print ('la entrada al parque es gratis')
elif age < 18:
	print ('la entrada para las edades entre 4 y 18 años es $5.')
else:
	print ('la entrada para mayores a 18 años es $10')

# solucion mas avanzada

age = 10
if age < 4:
	price = 0
elif age < 18:
	price = 5
else:
	price = 10
	
print ('El costo para ' + str(age) + 'años de edad es' + str(price)+'dolares')
