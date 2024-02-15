#Diccionarios

#get()
#Busca un valor a partir de su clave 

diccionario = {'Nombre':'Ana','Edad':35,'Profesion':'Administrativo'}
print(diccionario.get('Edad'))

#keys()
#Genera una lista con las claves del diccionario

print(diccionario.keys())

#values()
#Una lista con los valores del diccionario

print(diccionario.values())

#items()
#Devuelve las duplas clave/valor del diccionario en formato lista

print(diccionario.items())

#pop()
#Elimina una clave/valor en un diccionario

diccionario.pop('Nombre')
print(diccionario.items())

