players = ['charles', 'martina', 'michael', 'florence', 'eli']
# [indice : posicion en la lista]
print(players[1:4])

# indice 1 'martina' hasta el 4to elemento 'florence'
# ['martina', 'michael', 'florence']

# looping through a slice

print ("here are the first three players on my team:")
for player in players[:3]:
	print (player.title())
