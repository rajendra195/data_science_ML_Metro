"""
class => Entity

Example:


"""

class Car:
    def __init__(self, tyres, doors, window, engine_type): # constructer define
        self.tyres = tyres
        self.doors = doors
        self.window = window
        self.engine_type = engine_type
    
    def drive(self):
        print(f"The type of car is {self.engine_type}.")



# if __name__ == "__main__":
#     car_01 = Car(4, 4, 8, "petrol")
#     print(car_01)
#     car_01.drive()
        
class Animal:
    def __init__(self, *args):
        if len(args) == 1:
            self.name = args[0]
        elif len(args) == 2:
            self.name = args[0]
            self.species = args[1]
        elif len(args) == 3:
            self.name = args[0]
            self.species = args[1]
            self.age = args[2]

    def walk(self):
        print(f"{self.name} is walking.")

# if __name__ == "__main__":
#     # animal_01 = Animal(name="Human", species="Mammal")
#     # print(animal_01.name)
#     animal_02 = Animal("Dog","Mammal", 34)
#     print(animal_02.age)
#     animal_02.walk()
        
class Car:
    def __init__(self, door, window, engine_type):
        self.door = door
        self.window = window
        self.engine_type = engine_type

class Maruti(Car):
    def __init__(self, door, window, engine_type,  max_speed):
        self.max_speed = max_speed
        super().__init__(door, window, engine_type)

    def base(self):
        print(self.door, self.window, self.engine_type, self.max_speed)


if __name__ == "__main__":


    # car = Maruti(3, 43, "petrol", 222)
    # car.base()

    # parent = Car()

    child = Maruti(4, 5, "electric", 400)
    child.base()