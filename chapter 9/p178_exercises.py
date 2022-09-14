"""9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method."""

from p171_exercises import Restaurant
from p171_exercises import User
from p172_inheritance import Battery
from p172_inheritance import ElectricCar

class IceCreamStand(Restaurant):
	"""Sub Class IceCream"""
	def __init__ (self, name, cuisine_type):
		super().__init__(name, cuisine_type)
		self.flavors = ['vanilla','chocolat','lemon','sweet milk']


freedo = IceCreamStand('frido','heladeria')

print ("Our available flavors are:")
for sabor in freedo.flavors:
	print (f"- {sabor}")

"""9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method."""

class Admin(User):
	def __init__(self, first_name, last_name):
		super().__init__(first_name, last_name)
		# self.privileges = ['can add post','can delete post','can ban user']
		self.privileges = Privileges()
"""
	def show_privileges(self):
		print ('This kind of user has this privileges: ')
		for privilege in self.privileges:
			
			print (f"- {privilege.title()}") """


#new_user = Admin('Carlos','Rosas')
#new_user.show_privileges()

"""9-8. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges."""

class Privileges():
	def __init__(self, privileges=['can add post','can delete post','can ban user']):
		"""Initialize the Privileges attributes."""
		self.privileges = privileges

	def show_privileges(self):
		print ('This kind of user has this privileges: ')
		for privilege in self.privileges:
			
			print (f"- {privilege.title()}") 


new_user = Admin('Carlos','Rosas')
new_user.privileges.show_privileges()


"""9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
Add a method to the Battery class called upgrade_battery(). This method
should check the battery size and set the capacity to 85 if it isn’t already.
Make an electric car with a default battery size, call get_range() once, and
then call get_range() a second time after upgrading the battery. You should
see an increase in the car’s range."""

# The class Battery was modified in the module p172_inheritance.py
citroen_c3 = ElectricCar('citroen','c3',2016)
citroen_c3.battery.get_range()
citroen_c3.battery.upgrade_battery()
citroen_c3.battery.get_range()
