alien_0 = {}                # create an empty dictionary
alien_0['color'] = 'green'  # assign green value to key 'color'
alien_0['points'] = 5       # assign 5 value to key 'points'
print(alien_0)              # print the hole dictionary-

# >>>> output: 
#      alien_0 = {'color': 'green', 'points': 5}

## modifiying values in the diccionaries

alien_0 = {'color': 'green'}                            # assign again green to key color.
print("The alien is " + alien_0['color'] + ".")         # print the value 'green' for the key 'color'
alien_0['color'] = 'yellow'                             # reassign the value for 'color'
print("The alien is now " + alien_0['color'] + ".")     # check the change for the key color.

# Removing ket value pairs

alien_0 = {'color': 'green', 'points': 5} # dictionary recreated to avoid del error in the next line in case you run the code multiple times.
print(alien_0)

del alien_0['points']
print(alien_0)


favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}


print("Sarah's favorite language is " +
favorite_languages['sarah'].title() +
 ".")


people = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
