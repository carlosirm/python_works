"""8-6. City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
-----------------
"Santiago, Chile"
-----------------

Call your function with at least three city-country pairs, and print the value
that’s returned."""


def city_country(city, country):
	print (f"{city.title()}, {country.title()} ")


city_country('santiago','chile')

"""8-7. Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Add an optional parameter to make_album() that allows you to store the
number of tracks on an album. If the calling line includes a value for the number
of tracks, add that value to the album’s dictionary. Make at least one new
function call that includes the number of tracks on an album.
"""

def make_album(artist, title, track_qty=''):
	
	album = {'artist':artist,'title':title}
	album[track_qty]=str(track_qty)

	return album

new_album = make_album('Puff Daddy','I own you',8)
print (new_album)
new_album = make_album('Eminem','Street rap',10)

print (new_album)
new_album = make_album('Blink','Enema of state')

print (new_album)

"""8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop."""


def make_album(artist='', title=''):
	album = {artist:title}

	polling_active = True
	print ("Ingresa tu artista y album favorito. ")
	
	while polling_active:

		# Prompt for the person's name and response.
		artist = input("\nWhat is your favorite artist? ")
		albmname = input("Which is his/her album? ")
		# Store the response in the dictionary:
		album[artist] = albmname
		
		# Find out if anyone else is going to take the poll.
		repeat = input("Would you like to add another register? (yes/ no) ")
		if repeat == 'no':
			polling_active = False

	return album

new_album = make_album('rhcp','californication')

for key, value in new_album.items():
	print (f"{key} {value}")


