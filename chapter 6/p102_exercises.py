"""6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary."""

person = {'first_name':'Carlos', 'last_name':'Rosas','age':36, 'city':'Buenos Aires'}

print ('Ejercicio 6.1')
for row, value in person.items():
	
	print (row+': '+str(value))
print ('\n')

"""6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program."""

favorite_numbers = {'Lorenzo':7, 'Carlos':5, 'Lilene':3}
print ('Ejercicio 6.2')
for row, value in favorite_numbers.items():
	
	print ('El número favorito de ' + row + ' es el ' + str(value))
print ('\n')

"""6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
	• Think of five programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
	• Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output."""

glossary = {'python':'is a programming language',
			'aws':'it is a cloud computing provider',
			'vpn': 'virtual private network',
			'acl': 'access control list',
			'ec2': 'elastic cloud computing'}

for row, value in glossary.items():
	print (row + ':')
	print ('	'+value+'\n')
