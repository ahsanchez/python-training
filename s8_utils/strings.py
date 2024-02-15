#Strings

#upper() 
#Se usa para convertir una cadena a mayúscula

cadena = "Soy una cadena"
print(cadena.upper())

#lower()
#Devuelve una cadena en minúscula

print(cadena.lower())

#count()
#Nos dice cuantas veces aparece una subcadena en una cadena

print(cadena.count('a'))

#find()
#Nos devuelve el índice de la posición donde se encuentre la subcadena. Devuelve -1 si no está

print(cadena.find('Soy'))

#startswith()
#Devuelve True o False si la cadena empieza por la subcadena especificada

print(cadena.startswith('Soy'))

#endswith()
#Devuelve True o False si la cadena termina por la subcadena especificada

print(cadena.endswith('Soy'))

#split()
#Separa la cadena por el carácter especificado y devuelve una lista (útil para un string separado por comas)

cadena2 = "Hola, que, tal, todo"
print(cadena2.split(','))

#join()
#Une los caracteres de la cadena usando el carácter especificado 

print(",".join(cadena))

#strip()
#Quita los espacios en blanco por delante y detrás de una cadena

cadena3 = "           Soy una cadena   "
print(cadena3.strip())

#replace()
#Reemplaza una subcadena dentro de la cadena y la deuvelve

print(cadena.replace('a', 'u'))
