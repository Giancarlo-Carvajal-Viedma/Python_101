from class2 import Vehicles
from typing import List, Tuple
# print(type(1))
# print(type(""))


# Klasser brukar inte anvönda snake_case utan anvönder CapWord/PascalCase
class Animal:
    sound: str = "Grrrowwr"
    def __init__(self, sound: str):
        self.sound = sound
        pass

    def speak(self):
        print("I say " + self.sound)
        return "I say " + self.sound
    
    def change_sound(self, sound = str):
        self.sound = sound
    
    def get_sound(self):
        return self.sound


class ComputerScreen:
    pass


animal = Animal("")
cat = Animal("Meow")
dog = Animal("Voff")
fish = Animal("Blubb")
screen = ComputerScreen()
car = Vehicles()

# print(type(animal), type(screen), type(car))

animal.change_sound("Prassel")
animal.sound = "Groewwe"
# print (animal.sound)
# print (cat.sound)
# print (dog.sound)
# print (fish.speak())


class Company:
    name: str
    number_of_employees: int
    address: str
    CEO: str

    def __init__(self, name: str, number_of_employees: int, address: str, ceo: str):
        self.name = name
        self.address = address
        self.number_of_employees = number_of_employees
        self.CEO = ceo
    
    def __str__(self) -> str:
        name_string =f"Name: {self.name}"
        address_string =f"Address: {self.address}"
        employee_string =f"Employee: {self.number_of_employees}"
        ceo_string =f"CEO: {self.CEO}"
        return f"{name_string}, {address_string}, {employee_string}, {ceo_string}" 


class Person:
    first_name: str
    last_name: str
    age: int
    height: int
    full_name: str
    company: Company

    def __init__(self, first_name: str, last_name: str, age: int, height: int, company: Company):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.company = company
        self.full_name = f"{first_name} {last_name}"

    def __str__(self) -> str:
        return f"Hej jag heter {self.first_name} {self.last_name} Jag är {self.age} år gammal och {self.height} cm lång och jobbar på {self.company}"

    def __int__(self) -> int:
        return self.first_name.count("G")


gian = Person("Gian", "Carlo", 30, 170, Company(
    "Level", 1, "Stockholm", "Giancarlo"))

# hur man skapar multiline strängar 
message = """ Vi bakar bullar
på söndagar bakar vi bullar
på caffet"""
# print(gian.first_name)
# print(gian.full_name)
# # print(message)
# print(test)
# test = int(gian)
# print(gian)
# print(gian.company)




class Phone:
    number: str
    weight: int
    manufacturer: str
    color: str
    five_g_enabled: bool


    def __init__(self, number: str, weight: int, manufacturer: str, color: str, five_g_enabled: bool):
        self.color = color
        self.number = number
        self.weight = weight
        self.manufacturer = manufacturer
        self.five_g_enabled = five_g_enabled


class SmartPhone(Phone):
    apps: List[str]
    foldable: bool
    dimensions: Tuple[int, int]

    def __init__ (self, apps: List[str], foldable: bool, dimensions: Tuple[int, int], number: str, weight: int, manufacturer: str, color: str, five_g_enabled: bool):
        super().__init__(number, weight, manufacturer, color, five_g_enabled)
        self.apps = apps
        self.foldable = foldable
        self.dimensions = dimensions


my_phone = SmartPhone(["Candy crush", "Google Maps"], 
                      False, (6, 15), "070707070", 400, "Samsung", "Red", True)
# __dict__ gör en class till ett dict object, när vi sedan kallar print så görs dict objectet till en sträng 
print(my_phone.__dict__)