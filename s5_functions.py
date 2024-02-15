def myFunction():
    print("Hola")


def multiply():
    a = 5
    b = 4
    c = a * b
    print(c)


def validate(a, b):
    if a == b:
        return True
    else:
        return False


a = 2
b = 3
print("Adiós")
myFunction()
multiply()
print(validate(5, 4))

list = [1, 2, 3, 4]
numInput = int(input())

for num in list:
    if validate(num, numInput):
        print("Introduced number is in list")
        break
else:
    print("Introduce number is not in list")
