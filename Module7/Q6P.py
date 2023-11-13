# Jose Diaz 11/12/23
# Work of what we have
# we work of with what we got and introduced new attributes to the cars and methods
# additionally we print them to show the differences

# Q6





class Car:
    def __init__(self, model, year, color, car_type, manufacturer):
        self.model = model
        self.year = year
        self.color = color
        self.car_type = car_type
        self.manufacturer = manufacturer

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_car_type(self):
        return self.car_type

    def get_manufacturer(self):
        return self.manufacturer

    def fullspecs(self):
        return f"{self.manufacturer} {self.model} {str(self.year)} {self.color} {self.car_type}"
# we created the new attributes additionally to be able to call upon them later
car1 = Car("Sports", 2012, "Blue", "Super", "Links Motors")
car2 = Car("Sedan", 2020, "Black", "4 door sedan", "Chaos Cars")

# Print the new attributes that we created
print(car1.get_color())

print(car1.get_model())

print(car1.get_car_type())

print(car1.get_manufacturer())

# Print the new specification that we added to both cars
print(car1.fullspecs())

print(car2.fullspecs())
