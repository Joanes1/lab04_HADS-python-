
#Primer ejercicio:

from datetime import *

#Escribe el día de la semana actual (el de hoy)

hoy = datetime.now()
hoyNombre = hoy.strftime("%A")
print("El dia de la semana actual es:", hoyNombre)

print(" ")
print(" ")

#Solicita una fecha (en formato dd/mm/aaaa), indicando el día de la semana

print("Inserta una fecha con el siguiente formato: yyyy/mm/dd")
fecha = input("Fecha:  ")

print(datetime.strptime(fecha, "%Y/%m/%d").strftime("%A"))

print(" ")
print(" ")

#Como el anterior, pero el día de la semana escrito en castellano.

import locale

locale.setlocale(locale.LC_ALL,'es_ES.UTF-8')

print("Inserta una fecha con el siguiente formato: yyyy/mm/dd")
fecha_esp = input("Fecha:  ")

print(datetime.strptime(fecha_esp, "%Y/%m/%d").strftime("%A"))

print(" ")
print(" ")


#Pide una fecha de nacimiento y escribe: Cuántos años tiene el nacido en ese día y
#cuántos días, horas, minutos y segundos le faltan para el siguiente cumpleaños.

print("Inserta tu fecha de nacimiento con el siguiente formato: yyyy/mm/dd")
fecha_nacimiento = input("Fecha de nacimiento:  ")

def calcular_edad(a):
	año = int(a[:4])
	mes = int(a[5:7])
	dia = int(a[8:])
	if(datetime.now().year < año):
		return "Error.Fecha de nacimiento posterior a la fecha actual"
	elif(datetime.now().year == año):
		if(datetime.now().month < mes):
			return "Error.Fecha de nacimiento posterior a la fecha actual"
		elif(datetime.now().month == mes and datetime.now().day < dia):
			return "Error.Fecha de nacimiento posterior a la fecha actual"
		else:
			return 0		
	else:
		if(datetime.now().month < mes):
			return datetime.now().year - año - 1
		elif(datetime.now().month == mes and datetime.now().now < dia):
			return datetime.now().year - año - 1
		else:
			return  datetime.now().year - año 

edad = calcular_edad(fecha_nacimiento)
print("Tienes ", edad, " años")