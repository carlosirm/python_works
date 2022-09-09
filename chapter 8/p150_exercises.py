"""8-9. Magicians: Make a list of magician’s names. Pass the list to a function
called show_magicians(), which prints the name of each magician in the list."""

migician_names = ['ra','david cooperfield','christ angel']
great_magician = []

def show_magician(magician_list):
	for magician in magician_list:
		print (f"{magician.title()}")


#show_magician(migician_names) 

"""8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
Write a function called make_great() that modifies the list of magicians by adding
the phrase the Great to each magician’s name. Call show_magicians() to
see that the list has actually been modified."""

def show_magician(magician_list, great_magician):
	while magician_list:
		current_magician = magician_list.pop()
		great_magician.append(current_magician)
		
		

def make_great(great_magician):
	for magician in great_magician:
		print (f"Great {magician.title()}")

show_magician(migician_names, great_magician)
make_great(great_magician) 

"""8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the
function make_great() with a copy of the list of magicians’ names. Because the
original list will be unchanged, return the new list and store it in a separate list.
Call show_magicians() with each list to show that you have one list of the original
names and one list with the Great added to each magician’s name."""

make_great(migician_names[:]) 


