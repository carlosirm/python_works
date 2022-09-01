agregar un TAB  a la linea.
\t 
print("\tPython")
>>> Python 
print("\tPython")
>>>		Python

Agregar un ENTER a la linea

\n	
\n\t
Tambien se pueden combinar
print("Languages:\n\tPython\n\tC\n\tJavaScript")

Languages:
	Python
	C
	JavaScript

Eliminar espacios en blanco	
variable.rstrip()
variable.rstrip()


listas = ['element_1','element_2','element_N']

Copiar una lista
lista_nueva = lista_original [:]

Atencion !!! 
No es lo mismo 
lista_nueva = lista_original

Creacion de una lista recorriendo un for.
cubes = [value **3 for value in range(1,12)]
print (cubes)

No se puede iterar varias veces un objeto csv_

Multiline String
prompt =  "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "