class Car:
    brand = "Ford"

    def acelerate(self):
        print("Acelerating...")


car1 = Car()
car1.color = "verde"
car1.moto = "gasolina"

print(car1)
print(car1.color)
print(car1.brand)

car1.brand = "Audi"
print(car1.brand)
car1.acelerate()
