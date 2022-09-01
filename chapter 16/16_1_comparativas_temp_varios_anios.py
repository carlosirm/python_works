"""
16.1 Hacer una comparativa entre las temperaturas anuales maximas de  1991, 2005 y 2020 
"""

import csv 
from matplotlib import pyplot as plt

# preparacion del grafico
fig = plt.figure (dpi = 128, figsize = (10,6))
# format plot
plt.title ("Maximun Temperatures For 1991, 2005 and 2019", fontsize=24)
plt.xlabel ('', fontsize = 8)
fig.autofmt_xdate()
plt.ylabel  ("Temperatures (C)", fontsize = 12)
plt.tick_params (axis = 'both', which = 'major', labelsize = 4)

with open ('historico_temperaturas.csv', encoding = 'utf8') as f:
	reader = csv.reader(f)		# usar el metodo reader de la clase csv para leer el archivo 'f'
	header_row = next(reader)	# leer la primera linea del archivo 'f' almacenado en el objeto reader.

# creación de las listas que van a almacenar las fechas y valores maximos y minimos.
	
	reader_filtered = []
	months = []
	highs1991, highs2005, highs2019 = [],[],[]
	lows  = []
# creacion de una lista con los años de interes.
	yearSubList = [1991,2005,2019]
	current_year = yearSubList[0] # capturar el año inicial





	print (current_year)
	# recorrer el objeto reader para extraer los datos de interes.


	for row in reader:
		
		if int(row[0]) == yearSubList[0]:# 1991
			high = float(row[2])
			low = float(row[3])
			months.append(row[1])
			highs1991.append(high)

		elif int(row[0]) == yearSubList[1]:# 2005
			high = float(row[2])
			low = float(row[3])
			months.append(row[1])
			highs2005.append(high)

		elif int(row[0]) == yearSubList[2]:# 2019
			high = float(row[2])
			low = float(row[3])
			months.append(row[1])
			highs2019.append(high)

		#elif int(row[0]) in yearSubList:

			print ('construyendo las variables del grafico')
			
plt.plot (  highs1991, c = 'red') # graficar los valores maximos
plt.plot (  highs2005, c = 'blue') # graficar los valores maximos
plt.plot (  highs2019, c = 'green') # graficar los valores maximos
#plt.plot (dates, lows, c = 'blue') # graficar los valores minimos


print ('limpiando variables')
# limpieza de variables

months.clear()
#highs.clear()
lows.clear()

print ('consultando el nuevo año ' + row[0] )

#asignacion de nuevo current_year
current_year = int(row[0])
print ('current_year es:' + str(current_year) + ' y row[0] es ' + row[0])

print ('dibujar el grafico')
print (highs1991)
print (highs2005)
print (highs2019)
plt.show ()





