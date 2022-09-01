"""6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 102) by replacing your series of print
statements with a loop that runs through the dictionary’s keys and values.
When you’re sure that your loop works, add five more Python terms to your
glossary. When you run your program again, these new words and meanings
should automatically be included in the output."""

print ('Ejercicio 6.4')
glossary = {'python':'is a programming language',
			'aws':'it is a cloud computing provider',
			'vpn': 'virtual private network',
			'acl': 'access control list',
			'ec2': 'elastic cloud computing'}

for row, value in glossary.items():
	print (row + ':')
	print ('	'+value+'\n')


"""6-5. Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
• Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
• Use a loop to print the name of each river included in the dictionary.
• Use a loop to print the name of each country included in the dictionary."""

print ('Ejercicio 6.5')
rivers = {'orinoco':'venezuela',
			'parana':'argentina',
			'nilo':'egipto'}

for rio, pais in rivers.items():
	print ('El rio ' + rio.title() + ' corre a traves de ' + pais.title())
print ('\n')

"""6-6. Polling: Use the code in favorite_languages.py (page 104).
• Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
• Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll."""

print ('Ejercicio 6.6\n')

# hacer una lista de amigos y si tu amigo esta en la lista de lenguajes favoritos indicarle un saludo

friends = ['alonso','edward','javier','sarha']

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

for amigo in friends:
	if amigo in favorite_languages.keys():
		"""En este caso como mi amigo en la lista aparece en el diccionario, 
		lo uso para buscar su valor dentro de ese diccionario y recuperar el nombre del curso que ya tomo.""" 
		print (amigo.title() + ' Gracias por haber tomado el curso de ' + favorite_languages[amigo] )
	else:
		print (amigo.title() + ' Deberias inscribirte en algun curso')
print ('\n')


