"""8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments."""


print ("*** T-Shirt ***")

def make_shirt(size, text):
	print(f"This is your resume: You ordered a shirt size {size}")
	print(f"with the display text {text}")


make_shirt('M',"World's King")
make_shirt(size='M',text="World's King")



"""8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message."""
print ("\n*** Large Shirts ***")
def make_shirt(size='L', text='I love python'):
	print(f"This is your resume: You ordered a shirt size {size}")
	print(f"with the display text {text}")


make_shirt()
make_shirt('M')
make_shirt('S','Hello World')


print ("\n*** Cities ***")
"""8-5. Cities: Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country."""

def describe_city (city, country):
	print(f"{city.title()} is in {country.title()}")

describe_city('caracas', 'venezuela')