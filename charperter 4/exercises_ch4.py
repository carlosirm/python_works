#  counting to twenty.

for value in range(1,21):
	print (value)
	
# one milling 

# for value in range (1,1000001):
#	print (value)
	
	
# summing a milliong 

list_million = list(range(1,1000001))
print ('el minimo es: '+ str(min(list_million)))
print ('el maximo es: '+ str(max(list_million)))
print ('la suma de la lista es: '+ str(sum(list_million)))


# odd numbers 1 to 20
odd_numbers = list(range(1,20,2))
print (odd_numbers)

# threes 
threes = list(range(0,31,3))
for value in threes:
	print(value)
	
	
	
# cubes
numbers = list(range(1,11))
for cube in numbers:
	print ('El cubo de ' + str(cube) + ' es ' + str(cube**3))

print ('prueba carlos')
print (value)

# cube compresion.
cubes = [value **3 for value in range(1,12)]
print (cubes)
