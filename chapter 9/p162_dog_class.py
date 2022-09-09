class Dog():
	"""A simple attempt to model a dog."""
	def __init__(self, name, age):
		"""Initialize name and age attributes."""
		self.name = name
		self.age = age

	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(self.name.title() + " is now sitting.")
	
	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(self.name.title() + " rolled over!")

my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
# Se accede al atributo name bajo la forma objecto.atributo
# que luego se llama al metodo title. 
# objeto.atributo.metodo()
print("My dog is " + str(my_dog.age) + " years old.")


my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Coby',3)

your_dog.sit()
your_dog.roll_over()