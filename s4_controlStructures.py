# Conditionals
print("================ CONDITIONALS ================")

a = 5

if a == 2:
    print("A=2")
else:
    print("A!=2")

if a == 2:
    print("A=2")
elif a == 5:
    print("A==5")
else:
    print("A!=2 & A!=5")

name = "Ana"
age = 35

if name == "Ana" and age == 34:
    print("Her name is Ana and she is 34 years old")
elif name != "Ana" and age == 34:
    print("Her name is not Ana and she is 34 years old")
elif name == "Ana" and age != 34:
    print("Her name is Ana and she is not 34 years old")
else:
    print("Her name is not Ana and she is not 34 years old")


# Loop - for
print("================ LOOP - FOR ================")

names = ["Ana", "Pablo", "Vero", "Marta"]

for name in names:
    print(name)

people = []

ana = {"name": "Ana", "age": 34}
pablo = {"name": "Pablo", "age": 20}
people.append(ana)
people.append(pablo)

print(people)
for person in people:
    print(person["name"], person["age"])

myList = [1, 2, 3, 4]
for num in myList:
    num = num * 2
    print(num)
print(myList)

for i, num in enumerate(myList):
    myList[i] *= 2
print(myList)

# Loop - while
print("================ LOOP - WHILE ================")

a = "5"
while a != "5":
    a = input()

print("Hola")

cont = 0
while cont != len(myList):
    print(myList[cont])
    cont += 1
