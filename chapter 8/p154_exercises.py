"""8-12. Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sandwich
that is being ordered. Call the function three times, using a different number
of arguments each time."""

def sandwich(name, *ingredients):
	print (f"{name}, your sandwich has:")
	for ingredient in ingredients:
		print (f"- {ingredient}.")

sandwich('carlos', 'cebolla', 'pollo', 'tomate')
sandwich('mariana', 'carne', 'morron')

"""8-13. User Profile: Start with a copy of user_profile.py from page 153. Build
a profile of yourself by calling build_profile(), using your first and last names
and three other key-value pairs that describe you."""

def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('albert', 'einstein',
							location='princeton',
							field='physics')
print(user_profile)


carlos_profile = build_profile('carlos', 'rosas',
							location='UNEXPO',
							field='sistemas',
							document_type='dni',
							doc_num='6546546',
							nationality='south american',
							bloodtype='AAA')
print(carlos_profile)

"""8-14. Cars: Write a function that stores information about a car in a dictionary.
The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. Call the function
with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this one:
-------------------------------------------------------------------
car = make_car('subaru', 'outback', color='blue', tow_package=True)
-------------------------------------------------------------------
Print the dictionary that’s returned to make sure all the information was
stored correctly."""

def make_car (marca, modelo, **features):
	car = {}
	car['marca'] =  marca
	car['modelo'] = modelo
	for clave, valor in features.items():
		car[clave] = valor
	return car

car = make_car('chevrolet', 'blazer',
				clase='camioneta',
				uso='semi carga' ,
				color= 'plateado',
				placas= 'aaa123bb' )
print (car)