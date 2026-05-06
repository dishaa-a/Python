class Car:
    color = "red"
    def __init__(self, name):
        self.name = name
        print("Car object created")

c1 = Car("Toyota")
print(c1.color)
print(c1.name)