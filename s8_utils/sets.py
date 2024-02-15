#Conjuntos

#add()
#Añade un elemento al conjunto. Recordemos que los conjuntos solo tienen elementos únicos, por lo que si está repetido no lo añadirá

conjunto = set()
conjunto.add(3)
conjunto.add(5)
conjunto.add(1)
conjunto.add(4)
conjunto.add(6)
conjunto.add(1)
print(conjunto)

#discard()
#Elimina un elemento si existe

conjunto.discard(1)
print(conjunto)

#issubset()
#Comprueba si un conjunto pertenece a otro, es decir, si todos sus elementos están en el otro conjunto

conjunto2 = {4,6}

print(conjunto2.issubset(conjunto))

#union()
#Junta dos conjuntos

conjunto3 = {1,2,8}
conjunto4 = conjunto2.union(conjunto3)
print(conjunto4)

#diference()
#Encuentra los elementos no comunes entre conjuntos
print(conjunto.difference(conjunto3))


