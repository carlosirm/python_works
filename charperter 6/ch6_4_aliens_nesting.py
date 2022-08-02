

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}


aliens = [alien_0, alien_1, alien_2]

"""
for alien in aliens:
	print(alien)
"""
# un ejemplo mas relistico tendria mas de tres aliens. Vamos a crear una flota de 30 aliens usando el funcion range()

aliens = []

for alien_num in range(30):
	print (alien_num)
	new_alien = {'color': 'green', 'points': 5, 'speed':'slow'}
	aliens.append(new_alien)

# now let's modify some aliens and distribute between diferents kinds, green yelow and red.

for alien in aliens[0:3]:
	alien['color'] = 'yellow'
	alien['speed'] = 'medium'
	alien['points'] = 10

for alien in aliens[4:10]:
	alien['color'] = 'red'
	alien['speed'] = 'fast'
	alien['points'] = 15


print (aliens)