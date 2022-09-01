# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:

# a. Print the message, The first three items in the list are:. Then use a slice to
#    print the first three items from that program’s list.

players = ['charles', 'martina', 'michael', 'florence', 'eli','tomas','ericson','joan','helena']

print ("here are the first three players on my team:")
for player in players[:3]:
	print (player.title())

# Print the message, Three items from the middle of the list are:. Use a slice
# to print three items from the middle of the list.

print ('Los items del medio de mi lista son: ')
for player in players [3:6]:
	print (player.title())
	
# Print the message, The last three items in the list are:. Use a slice to print
# the last three items in the list.

print ('Los ultimos tres items de mi lista son: ')
for player in players [6:9]:
	print (player.title())
