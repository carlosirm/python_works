
string = 'abcdecba'
string_bkp = string[:]

def is_palindrome (string):
	set_string = list(set(string))
	impar = 0
	print (set_string)
	for letter in set_string:
		print (f"variable string: {string}")
		print (f'buscando la letra {letter}')
		print (f'cantidad de veces encontrada {string.count(letter)}')
		if string.count(letter) % 2 == 1:
			impar += 1
			print (f'letra impar {letter}')
		
	if impar > 1:
		return 'NO'	
	else:
		return 'YES'
		


print (is_palindrome(string))