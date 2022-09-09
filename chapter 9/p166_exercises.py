"""9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating
that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes
individually, and then call both methods."""


class Restaurant():
	"""Restaurant"""
	def __init__ (self, name, cuisine_type):
		self.name = name
		self.cuisine_type = cuisine_type

	def describe_restaurant (self):
		print (f"Welcome to the {self.name} Restaurant")
		print (f"Here you'll find {self.cuisine_type} food")

	def open_restaurant(self):
		print (f"The {self.name} now is open")

"""
oneTown = Restaurant('One Town','Chinese')
oneTown.describe_restaurant()
oneTown.open_restaurant()"""

"""9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance."""
"""
restTwo = Restaurant('Miami Bar','American')
restTwo.describe_restaurant()
restTwo.open_restaurant()


restThree = Restaurant('Avila Burger','Venezuelan Burgers')
restThree.describe_restaurant()
restThree.open_restaurant()
"""

"""9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user."""

class User():
	def __init__(self, first_name, last_name):
		self.first_name =first_name
		self.last_name =last_name

	def describe_user(self):
		print (f"First Name: {self.first_name.title()}")
		print (f"Last Name: {self.last_name.title()}")
	
	def greet_user(self):
		print (f"Hello {self.first_name.title()} {self.last_name.title()}")

carlos = User('Carlos', 'Rosas')
lilene = User('Lilene', 'Sarmiento')
lorenzo = User('Lorenzo', 'Rosas')


carlos.describe_user()
carlos.greet_user()

lilene.describe_user()
lilene.greet_user()

lorenzo.describe_user()
lorenzo.greet_user()