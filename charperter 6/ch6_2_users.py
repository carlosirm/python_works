# Looping through all key-value pairs

users_0 = {
	'username':'efermi',
	'first':'enrico',
	'last':'fermi'
	}

for key, value in users_0.items():
	print ("\nKey: " + key)
	print ("Value: " + value)


# Ahora lo voy a presentar para que salga asi

# username: efermi
# first: enrico
# last: fermi

for key, value in users_0.items():	# key and value are variables. It could be perfectly param / string for example.
	print ( key + ":" + value)