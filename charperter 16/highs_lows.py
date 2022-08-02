import csv
from matplotlib import pyplot as plt

filename = 'historico_temperaturas.csv'
with open (filename, encoding = 'utf8') as f: # with maneja automaticamente el cierre del archivo.
		reader = csv.reader(f)
		header_row = next(reader)
		print (header_row)

		#enable only for index and column information.

		#for index, column_header in enumerate (header_row): #usa el par indice / nombre columna del header_row para identificar las posiciones/info del csv.
		#	print (index, column_header)


		#get high temperatures from file. Position 2 in my csv file historico_temperaturas.

		dates, highs, lows = [],[],[]
		
		for row in reader:
			if int (row[0]) in range (2010,2020): # comprobar si el año esta en el rango de los ultimos 10 años.
				try:
					#if int (row[0]) in range (2010,2020): # comprobar si el año esta en el rango de los ultimos 10 años.
						# months.append( row[1]) # agregar el valor del mes actual.
						# agregamos el año mes para que grafique los ultimos 120 meses (12 meses * 10 años)
					dates.append (row[0] + ' ' + row[1])
					high = float (row[2]) # agregar el valor max temperatura
					low = float (row[3])
						
				except ValueError:
					print (dates, 'DataError')
				else:
					lows.append(low)
					highs.append(high)



		print (str(highs)) # just for control.

# plot data
fig = plt.figure (dpi = 128, figsize = (10,6))
plt.plot (dates, highs, c = 'red') # graficar los valores maximos
plt.plot (dates, lows, c = 'blue') # graficar los valores minimos

# format plot
plt.title ("Agregate Temperatures Max and Min, Decade 2010 - 2020", fontsize=24)
plt.xlabel ('', fontsize = 8)
fig.autofmt_xdate()
plt.ylabel  ("Temperatures (C)", fontsize = 12)
plt.tick_params (axis = 'both', which = 'major', labelsize = 2)

plt.show ()