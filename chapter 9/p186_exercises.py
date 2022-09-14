"""9-13. OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you
used a standard dictionary to represent a glossary. Rewrite the program using
the OrderedDict class and make sure the order of the output matches the order
in which key-value pairs were added to the dictionary."""

from collections import OrderedDict
glossary = OrderedDict()
print ('Ejercicio 6.4')

glossary = {'python':'is a programming language',
			'aws':'it is a cloud computing provider',
			'vpn': 'virtual private network',
			'acl': 'access control list',
			'ec2': 'elastic cloud computing'}

for row, value in glossary.items():
	print (row + ':')
	print ('	'+value+'\n')


"""9-14. Dice: The module random contains functions that generate random numbers
in a variety of ways. The function randint() returns an integer in the
range you provide. The following code returns a number between 1 and 6:
--------------------------
from random import randint
x = randint(1, 6)
--------------------------
Make a class Die with one attribute called sides, which has a default
value of 6. Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has. Make a 6-sided die and roll
it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""

from random import randint

class Die():
	def __init__ (self, sides=6):
		self.sides = sides

	def roll_dice(self):
		num = randint(1,self.sides)
		print (num)



dado = Die()
dado.roll_dice()
dado.roll_dice()
dado.roll_dice()
dado.roll_dice()
dado.roll_dice()


dadoDiezLados = Die(10)
dadoDiezLados.roll_dice()
dadoDiezLados.roll_dice()
dadoDiezLados.roll_dice()
dadoDiezLados.roll_dice()
dadoDiezLados.roll_dice()
dadoDiezLados.roll_dice()


dadoVeinteLados = Die(20)
dadoVeinteLados.roll_dice()
dadoVeinteLados.roll_dice()
dadoVeinteLados.roll_dice()
dadoVeinteLados.roll_dice()
dadoVeinteLados.roll_dice()
