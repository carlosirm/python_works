# Looping through all the keys in a dictionary

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

for names in favorite_languages.keys():
    print (names)

# hacer una lista de amigos y si tu amigo esta en la lista de lenguajes favoritos indicarle un saludo

friends = ['alonso','edward']

for name, lenguage in favorite_languages.items():
    if name in friends:
        print ('Hola ' + name + ', veo que tu lengaje favorito es ' + lenguage)