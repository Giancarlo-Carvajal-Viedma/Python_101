from typing import Callable

# Functions in functions


def function_one():
    print("Function one called")
    return "Function one returned"


# function_one()

# En funktion kan sparas i en variabel
function_three_that_is_function_one = function_one

# Den variabeln kan sedan anropas för att anvönda funktionen
# function_three_that_is_function_one()


def function_two(inner_function: Callable = None):
    print("Function two called")
    print("Before inner function")
    print (inner_function())
    print("After inner function")


# function_two(inner_function=function_one)

# function_two(inner_function=lambda: "Hello from lambda")

# Lambda functions


# @function_two
# def function_4():
#     print("Function 4 called")


# @dataclass
# class MyClass:
#     a: str
#     b: int
#     c: float
#     pass

# my_object = MyClass()


# Closure / scope



res =90


def a():
    res = 0
    for i in range(2):
        res += i

    print(res)
    return res


# print(res)
# res = a()
# print(res)


# def decorator(inner_func: Callable):

#     def wrapper(args, **kwargs):
#         return a
#     return wrapper


# @decorator
# def add(b: int):
#     return


# List, dict comprehension

list = [{"name": "Gian", "age": 30}, {"name": "Pelle", "age": 40}, 
        {"name": "Stefan", "age": 45}, {"name": "Evert", "age": 90}]

# Ta namnet för varje person och lägg i en ny lista
names = [person["name"] for person in list]

# Ta åldern för varje person och lägg i en ny lista
ages = [person["age"] for person in list]


first_letters = [name[0] for name in names]
all_letters = ["Hola" + letter for name in names for letter in name]

# print (names)
# print (ages)
# print (first_letters)
# print (all_letters)

# Skapar en dict med name som key och age som valuet
dicts = {names[x]: ages[x] for x in range(len(names))}


# print (dicts)

# while loops, conditions, if statements

# counter = 0
# while True:
#     if counter > 10:
#         break
#     print("I am true with break", counter)
#     counter += 1

# # Vi måste påverka vårat condition i vår loop, vi kan ha fler conditions
# name = "Hola"
# counter = 0
# while counter <= 10 or name != "Gian":
#     print("I am true with condition", counter)
#     if counter == 5:



# funktioner med args och kwargs
def major_function(*args, **kwargs):
    print("Major function")
    print(args, kwargs)
    pass


def generall_function(name, *args, **kwargs):
    print(args,kwargs)
    surname, *rest= args
    fisk = kwargs['fisk']
    print(name, surname, fisk, rest)
    major_function(*rest, **kwargs)
    pass


generall_function("Gian", "Carlo", "är", "inte", 
                  "Pigg", "på", "morgonen", fisk="Gös")