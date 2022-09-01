"""6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person."""

people =[]
person1 = {'first_name':'Carlos', 'last_name':'Rosas','age':36, 'city':'Caracas'}
person2 = {'first_name':'Lilene', 'last_name':'Sarmiento','age':35, 'city':'Barranquilla'}
person3 = {'first_name':'Lorenzo', 'last_name':'Rosas','age':2, 'city':'Buenos Aires'}

print (person1['first_name'])

people = [person1, person2, person3]

print ('Ejercicio 6.7')
for persona in people:
	for row, value in persona.items():
		print (row+': ' + str(value))
print ('\n')

"""6-8. Pets: Make several dictionaries, where the name of each dictionary is the
name of a pet. In each dictionary, include the kind of animal and the owner’s
name. Store these dictionaries in a list called pets. Next, loop through your list
and as you do print everything you know about each pet."""

print ('Ejercicio 6.8')

toby = {'kind':'dog', 'owner':'scoty'}
laly = {'kind':'cat', 'owner':'Myra'}
piolin = {'kind':'bird', 'owner':'stella'}


pets = [toby, laly, piolin]

for pet in pets:

	for row, value in pet.items():
		print (row + ': ' + value)

"""6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
names to use as keys in the dictionary, and store one to three favorite places
for each person. To make this exercise a bit more interesting, ask some friends
to name a few of their favorite places. Loop through the dictionary, and print
each person’s name and their favorite places."""

print ('Ejercicio 6.9')

favorite_places = {'Carlos':['Caracas','Buenos Aires','Mendoza'],
					'Lilene':['Medellin','Bariloche','Curazao'],
					'Lorenzo':['Caracas','Medellin','Calafate']}

for key_names, city_values  in favorite_places.items():
	print (key_names + ' Your favorite_places are: ')
	for cv in city_values:
		print ( cv) 
	 
"""6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers."""

favorite_numbers = {'Lorenzo':[7,3,1], 'Carlos':[5,7,11], 'Lilene':[1,2,3]}
print ('Ejercicio 6.10')
for row, value in favorite_numbers.items():
	
	print ('Los números favoritos de ' + row + ' son:')
	for val in value:
		print (str(val))
print ('\n')


"""6-11. Cities: Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the information
you have stored about it.
"""
cities = {'caracas':{'Country':'Venezuela',
					'population':'4 Millions',
					'fact':'its a very fresh city and it is in front of Carebean Sea.'},
			'buenos Aires':{'Country':'Argentina',
					'population':'6 Millions',
					'fact':'It is in south america and its known as the meats land'},
			'new York':{'Country':'United States',
					'population':'10 Millions',
					'fact':'Apples world and has a lot of people living there.'},
					}
for city_key, city_value in cities.items():
	print (city_key.title())
	for atribute_key, atribute_value in city_value.items():
		print ('\t'+atribute_key.title()+': ' + atribute_value)
