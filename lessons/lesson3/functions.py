# Jan 9, 2023 # Funktioner
#Indentering 
# Funktioner 
# Definition 
# Parametrar 
# Argument (position, namngivning)
from typehints_typings import my_function as my_imported_function
def my_function(name,surname, *rest) -> None: #Funktion oftast är att behandla en input och en output # name=parameter
   # print ("In my function ", rest)
    return "Hej " + name


my_function("Gian ", "Carlo", 1) #Allt i python är object, classer, functioner mm
# print(my_function("Gian"))


def a_general_function(x, y, *args, is_employed= False, **kwargs): #arguments skrivs med ett * och kwargs med två **
    # a, b, c, d, e, f, g  = args
    a, b, c, d, e  = args
    print(kwargs["name"])
    print(is_employed)
    # print(a, g)
    print(a, e)
    print(args, kwargs) # Args(arguments):tuple #kwargs(keywordArguments):dict


# a_general_function("A", "B", 1, 2, 3, True, False, name="Gian")


def generate_person(name, surname, *attributes, is_employed=False, hobbies=[], **kwargs):
    print(name, surname, "is a person with ", attributes)
    print(name, " is ")
    if is_employed:
        print("Employed")
    else:
        print("Unemployed")
    
    print("Hobbies are:")
    for hobby in hobbies:
        print(hobby)
    
    print("Other info")
    for key, value in kwargs.items():
        print(key, value)


# generate_person("Gian", "Carlo", "Patient", 
#                "Smart", "Intelligent", is_employed=True, hobbies=["Python", "Java", "C++", "Code"], magnificent=False)

# Functions with no *


def function_wthout_catchallargs(pos1=None, pos2=None, kw1=None, kw2=None, **kwargs): #Positionella args måste alltid komma först!
    # print(pos1, pos2, kw1, kw2, kwargs)
    pass # Betyder pass denna function, skipa den och gå vidare


# function_wthout_catchallargs("A", "B", kw1="Hej", kw2="Hej då")
# function_wthout_catchallargs(pos1="A", pos2="B", kw1="Hej", kw2="Hej då")
# function_wthout_catchallargs("A", "B", "Hej", "Hej då")

# Functions with no **


def function_wthout_catchallargs(pos1, pos2=None, kw1=None, kw2=None):
    # print(pos1, pos2, kw1, kw2)
    pass


# function_wthout_catchallargs(pos1="Gian", kw2="Kalle")
# function_wthout_catchallargs(kw2="Kalle") # Funkar inte då på line 64 är positionen ej definierat (=None)!

def a_function_that_return_an_int():
    return 1


def a_function_that_return_an_string():
    return "Hej jag heter Gian"


# print(a_function_that_return_an_int(), type(a_function_that_return_an_int()))
# print(a_function_that_return_an_string(), type(a_function_that_return_an_string()))


def a_function_that_return_an_list(a, b, c):
    return [a, b, c]


my_list = a_function_that_return_an_list(1, 2, 3)
# print(my_list)
# print(a_function_that_return_an_list("hej","på","dig"))


def a_function_that_return_an_tuple(a, b, c):
    return (a, b, c)


# my_tuple = a_function_that_return_an_tuple("A", "B", "C")
value1, value2, value3 = a_function_that_return_an_tuple("A", "B", "C")
# print(my_tuple)
# print(value1)
# print(value3)


def add_value(value1, value2, *args):
    result = value1 + value2
    for value in args:
        result += value

    return result
    

my_result = add_value(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
my_result2 = add_value("a", "b", "c", "d")
# print(my_result)
# print(my_result2)

# funktioner är i sig också objekt
# vilket betyder att en funktion kan skickas till en funktion som argument


class MyClass():
    a: int

    def __init__(self):
        print("Hej från klass")


def func1():
    print("func1")


def func2(a):
    a()
    print(a)



func2(MyClass)

# my_imported_function()
