class Figure:

    def __init__(self, numSides, long) -> None:
        self.numSides = numSides
        self.long = long

    def calculatePerimeter(self):
        return self.numSides * self.long


pyramid = Figure(4, 8)
permiter = pyramid.calculatePerimeter()
# print(permiter)


class User:

    def __init__(self, name, pin, balance) -> None:
        self.name = name
        self.pin = pin
        self.balance = balance


class Bank:

    def __init__(self, users=[]) -> None:
        self.users = users

    def authenticate(self, name, pin):
        for user in self.users:
            if user.name == name:
                if user.pin == pin:
                    print("You are logged!")
                    return True
                else:
                    print("Authetication failed!")
                    return False
            else:
                print("User not found!")
                break

    def withdrawMoney(self, name, money):
        for user in self.users:
            if user.name == name:
                if user.balance < money:
                    print("Insuficient balance!")
                    break
                elif user.balance >= money:
                    user.balance = user.balance - money
                    print("Current balance: " + str(user.balance))
                    break


ana = User("Ana", "7450", 450000)
vero = User("Verónica", "1110", 40000)
bea = User("Beatriz", "2268", 10)

bank = Bank(users=[ana, vero, bea])
# bank.authenticate("Ana", 7450)
# bank.authenticate("Ana", 1230)
# bank.authenticate("Luis", 7450)

while True:
    print("Welcome! Please, authenticate.")
    print("Name: ")
    name = input()
    print("Pin: ")
    pin = input()
    if bank.authenticate(name, pin):
        while True:
            print("Pleae, select an option. \n1. Withdrow money\n2.End session")
            option = input()
            if option == "1":
                print("Amount: ")
                money = input()
                bank.withdrawMoney(name, int(money))
            elif option == "2":
                print("Exit.")
                break
            else:
                print("Wrong option.")
    else:
        print("Authentication failed. Please, give a right name and pin.")
