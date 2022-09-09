"""9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number
you like that could represent how many customers were served in, say, a
day of business."""

class Restaurant():
	"""Restaurant"""
	def __init__ (self, name, cuisine_type):
		self.name = name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant (self):
		print (f"Welcome to the {self.name} Restaurant")
		print (f"Here you'll find {self.cuisine_type} food")

	def open_restaurant(self):
		print (f"The {self.name} now is open")

	def print_customers_number(self):
		print (f"This restaurant has serve to {self.number_served} customers")

	def set_number_served(self, new_number):
		self.number_served = new_number

	def increment_number_served(self, new_number):
		self.number_served += new_number


"""
restaurant = Restaurant('One Town','Chinese')
restaurant.print_customers_number()

restaurant.number_served = 12
restaurant.print_customers_number()

restaurant.set_number_served(20)
restaurant.print_customers_number()

restaurant.increment_number_served(10)
restaurant.print_customers_number()"""


"""9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166). Write a method called increment_
login_attempts() that increments the value of login_attempts by 1. Write
another method called reset_login_attempts() that resets the value of login_
attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0."""

class User():
	def __init__(self, first_name, last_name):
		self.first_name =first_name
		self.last_name =last_name
		self.login_attempts = 0

	def describe_user(self):
		print (f"First Name: {self.first_name.title()}")
		print (f"Last Name: {self.last_name.title()}")
	
	def greet_user(self):
		print (f"Hello {self.first_name.title()} {self.last_name.title()}")

	def increment_login_attempts(self):
		self.login_attempts += 1
		print (f"Current login attempts: {self.login_attempts}")

	def reset_login_attempts(self):
		self.login_attempts = 0
		print (f"The loggin attempts has been reseted to 0")

"""
carlos = User('Carlos', 'Rosas')
lilene = User('Lilene', 'Sarmiento')
lorenzo = User('Lorenzo', 'Rosas')


carlos.describe_user()
carlos.increment_login_attempts()
carlos.increment_login_attempts()
carlos.increment_login_attempts()
carlos.reset_login_attempts()
carlos.increment_login_attempts()
"""