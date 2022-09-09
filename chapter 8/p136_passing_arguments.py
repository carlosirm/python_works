
def describe_pet(animal_type, pet_name):

	"""Display information about a pet."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# positional arguments
describe_pet('hamster', 'harry')

# keyword arguments
describe_pet(animal_type = 'hamster', pet_name = 'harry')

# keyword arguments interchangeable
describe_pet( pet_name = 'harry', animal_type = 'hamster')


 # function with default parameter
def describe_pet_2 (pet_name, animal_type='dog'):
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet_2('spot')