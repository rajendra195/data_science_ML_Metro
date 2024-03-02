""" Private Access """
class Person:
    def __init__(self, name, age):
        # private attribute
        self.__name = name
        self.__age = age


    def display(self):
        print(f"The person name is {self.__name} is {self.__age} years old.")

    
class Ram(Person):
    def __init__(self, name, age, address):
        super().__init__(name, age)
        self._address = address

    def display(self):
        print(f"The person name is {self.name} is in {self._address} and is {self.age} years old.")

# if __name__ == "__main__":
#     # person_test = Person(name="Ram", age=22)
#     # person_test.display()
#     # print(person_test._Person__name)

#     person2 = Ram(name="Har", age=33, address="Bhaktapur")
#     person2.display()
        
# Abstraction
        