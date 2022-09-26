class Toyota:
    def __init__(self, model, engine, gear, color):
        self.model = model
        self.engine = engine
        self.gear = gear
        self.color = color

    def __str__(self):
        return f"Toyota {self.model}; Engine: {self.engine}; Color: {self.color}; Gear: {self.gear}"

    def change_color(self, new_color):
        self.color = new_color

    def drive(self):
        print("Vzzhhh!")

    def shift_gear(self, new_gear):
        self.gear = new_gear


car1 = Toyota("T1", "Eng1", 6, "White")
car2 = Toyota("T2", "Eng_plus", 7, "Orange")
car3 = Toyota("T3", "Eng_small", 4, "Sea_color")

print(car1)
print(car2)
print(car3)

car1.shift_gear(5)
car2.change_color("Brown")

print(car1)
print(car2)
print(car3)

car2.drive()
