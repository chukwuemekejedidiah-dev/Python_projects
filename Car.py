class Car:
    def __init__(self, model, color, brand, year):
        self.model = model
        self.color = color
        self.brand = brand
        self.year = year

    def drive(self):
        print(f"Mode: {self.model}, Color: {self.color}, Brand: {self.brand}, Year: {self.year}")


toyota = Car("Toyota", "Blue", "Jeep", "2020")
rangeRover = Car("RangeRover", "Red", "Velar", "2020")
landRover = Car("LandRover", "Green", "Jeep", "2020")
mercedes = Car("Mercedes", "Blue", "Jeep", "2020")


print(toyota.model)
print(rangeRover.model)
print(landRover.model)
print(mercedes.model) 