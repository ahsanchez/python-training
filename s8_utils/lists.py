#Listas

#append()
#Añade un elemento al final de la lista

lista = [1,2,3,4,5]
lista.append(0)
print(lista)

#extend()
#Une una lista a otra

lista2 = [8,9,2,0,3]
lista.extend(lista2)
print(lista)

#count()
#Como en los strings, cuenta el número de veces que aparece un elemento

lista = ['Hola', 'Hola', 'que', 'tal']
print(lista.count("Hola"))

#index()
#Devuelve el índice de un elemento en la lista. Si exite varias veces, devuelve la primera vez que aparece

print(lista.index("Hola"))

#insert()
#Inserta un elemento en la posición especificada

lista.insert(2, "Soy una inserción")
print(lista)

#pop()
#Elimina el elemento cuyo índice le especifiquemos y nos lo devuelve

print(lista.pop(1))
print(lista)

#remove()
#Borra el elemento cuyo valor le especifiquemos
lista.remove("Hola")
print(lista)

#sort()
#Ordena la lista de menor a mayor

lista = [1,2,3,-9,18,13,-3]
lista.sort()
print(lista)

#Podemos ordenarla de mayor a menor usando reverse en el sort

lista.sort(reverse=True)
print(lista)
