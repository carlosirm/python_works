# 5-10. Checking Usernames: Do the following to create a program that simulates
# how websites ensure that everyone has a unique username.
# • Make a list of five or more usernames called current_users.
# • Make another list of five usernames called new_users. Make sure one or
# two of the new usernames are also in the current_users list.
# • Loop through the new_users list to see if each new username has already
# been used. If it has, print a message that the person will need to enter a
# new username. If a username has not been used, print a message saying
# that the username is available.
# • Make sure your comparison is case insensitive. If 'John' has been used,
# 'JOHN' should not be accepted



current_users = ['Crosas','alviaresm','rodriguezm','burguilloa','olsenf','caniggiam','admin']
crnt_users_lwcs = [x.lower() for x in current_users] # copia la lista de usarios a otra lista con todo en minusculas.

new_users = ['piag','hildar','camiloS','pedror','jimmyv','CROSAS']

for new_user in new_users:
	if new_user.lower() in crnt_users_lwcs:
		print ("Disculpe, este usuario '" + new_user + "' ya esta en uso")
	else:
		print("Este nombre de usuario '" + new_user + "' esta disponible ")
		
