class Car:
    def __init__(self, color, miles):
        self.color = color
        self.miles = miles

    def __str__(self):
        return f"{int(self.miles)} and {self.color}."
    
car1 = Car('Black', 24)
print(car1)