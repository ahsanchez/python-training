class Car:
    def __init__(self, brand, color, motor):
        self.brand = brand
        self.color = color
        self.motor = motor

    def __str__(self):
        return (
            "Brand: " + self.brand + ", color: " + self.color + ", motor: " + self.motor
        )


class SportCar(Car):
    speedMax = "250 km/h"

    def __str__(self):
        return (
            "Brand: "
            + self.brand
            + ", color: "
            + self.color
            + ", motor: "
            + self.motor
            + ", speed max: "
            + self.speedMax
        )


car1 = Car("Seat", "Blanco", "Gasolina")
print(car1)

audi = SportCar("Audi", "Verde", "Diésel")
print(audi)
