# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 60). Make a copy of the list of pizzas, and call it friend_pizzas.


pizzas = ['pepperoni','napolitana','primavera']
friend_pizzas = pizzas[:]


# Then, do the following:
# a. Add a new pizza to the original list.

pizzas.append('4 quesos')

# b. Add a different pizza to the list friend_pizzas.

friend_pizzas.append('hawaiana')
# c. Prove that you have two separate lists. Print the message, My favorite
# pizzas are:, and then use a for loop to print the first list. Print the message,
# My friend’s favorite pizzas are:, and then use a for loop to print the second
# list. Make sure each new pizza is stored in the appropriate list.

print ('My favorite pizzas are:')
print (pizzas)


print ('\nMy friends pizzas are:')
for f_pizza in friend_pizzas:
	print(f_pizza.title())
