magicians = ['Alice','David','Carolina']
for magician in magicians:
	print (magician)


for magician in magicians:
	# debe existir sangria para que python lo considere parte del loop
	print (magician.title() + ", That was a great trick")
	print("I can't wait to see your next trick, " + magician.title() + ".\n")
