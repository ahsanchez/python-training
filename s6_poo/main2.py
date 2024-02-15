class Car:
    def __init__(self, brand, color, motor):
        self.brand = brand
        self.color = color
        self.motor = motor

    def __str__(self):
        return (
            "Brand: " + self.brand + ", color: " + self.color + ", motor: " + self.motor
        )


class Concessionaire:

    def __init__(self, cars=[]):
        self.cars = cars

    def listCars(self):
        for car in self.cars:
            print(car)


car1 = Car("Seat", "Blanco", "Gasolina")
car2 = Car("Hyundai", "Azul", "Gasolina")

concessionaire = Concessionaire(cars=[car1, car2])
concessionaire.listCars()
