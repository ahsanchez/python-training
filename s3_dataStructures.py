# list

print("================ LISTS ================")
a = [1, 2, 3, 4]

print(a)
print(a[0])
print(a[3])
print(a[0:2])

b = [5, 6]

c = a + b

print(c)

a[2] = "Hola"
print(a)

a.append("Adiós")
print(a)

print(3 in a)
print("Hola" in a)
print("Ana" not in a)

# tuples: inmutables --> sus valores no se pueden modificar
print("================ TUPLES ================")

t = (1, 2, 3, 4)

print(t)
print(t[0])
print(t[3])
print(t[0:2])

print(3 in t)
print("Hola" in t)
print("Ana" not in t)

tToList = list(t)
print(tToList)
tToList.append("Nuevo valor")
print(tToList)

# sets
print("================ SETS ================")

set1 = {1, 2, 3, 4}

print(set1)
set1.add(8)
set1.remove(2)
print(set1)
print(2 in set1)
print(2 not in set1)

# dictionaries (mapas --> k,v)
print("================ DICTIONARIES ================")

car = {"brand": "ford", "color": "red"}
print(car)

print(car["color"])
car["color"] = "white"
print(car)
