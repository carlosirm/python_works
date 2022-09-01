# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.
# a. Use a for loop to print each food the restaurant offers.

basic_foods = ('bife de chorizo','milanesa de pollo','ensalada cesar','sopa de verduras','choripan')
print ('Menu original')
for food in basic_foods:
	print (food)
# b. Try to modify one of the items, and make sure that Python rejects the
# change.

# basic_foods[0] = 'ojo de bife' linea comentada

# c. The restaurant changes its menu, replacing two of the items with different
# foods. Add a block of code that rewrites the tuple, and then use a for
# loop to print each of the items on the revised menu.

print ('\nMenú modificado:')
basic_foods = ('ojo de bife','pollo guisado','ensalada caprese','sopa de verduras','bondiola')
for food in basic_foods:
	print(food)
