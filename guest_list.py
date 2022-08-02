guest_list = ['Juan','Pedro','Almodena','Jhon','Stephen']
print (guest_list)


mensaje = ', bienvenido al curso introductorio de Python'
print (guest_list[0] + mensaje)
print (guest_list[1] + mensaje)
print (guest_list[2] + mensaje)
print (guest_list[3] + mensaje)
print (guest_list[-1] + mensaje)

invitacion = ', estas cordialmente invitado a la cena de bienvenida del curso python'
print("\n \n")
print (guest_list[0] + invitacion)
print (guest_list[1] + invitacion)
print (guest_list[2] + invitacion)
print (guest_list[3] + invitacion)
print (guest_list[-1] + invitacion)

print ('Ahora ' + guest_list[0], 'no puede asistir.')
print('Eliminando de la lista a ' + guest_list[0])
removido = guest_list.pop(0)
lista_removidos=[]
lista_removidos.append (removido) 
print("\n")
print (str(lista_removidos) + ', fue eliminado de la lista')
print("\n")
print ('ahora la lista es' + str(guest_list))

nuevo_invitado = 'Braulio'
print('El nuevo invitado es ' + nuevo_invitado);
guest_list.append(nuevo_invitado)

del nuevo_invitado ## limpiando la lista de invitados.
print ('Los invitados son ' + str(guest_list))

print('Ahora se suman nuevos invitados dado que hay una mesa mas grande')
nuevo_invitado = ['Juana','Karla','Patricia']
print('Las nuevas invitadas son' + str(nuevo_invitado))

guest_list.insert(0,nuevo_invitado[0])
guest_list.insert(0,nuevo_invitado[1])
guest_list.insert(0,nuevo_invitado[2])
nuevo_invitado=[]

print("\n")
print ('ahora la lista es' + str(guest_list))

