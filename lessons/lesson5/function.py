def a_function():
    print("a_function")


def another_function():
    print("Another function")


a_variable = a_function
# another_function = a_function


# a_function()
# another_function()
# a_variable()

# print(a_function, a_variable)

def first_function(a):
    a(1, 2)
    print("First function", a)


def second_function(a, b):
    print("Second function")
    return "Hola"


# first_function("Hej")
# first_function(second_function)


# en lambda-function är en anonym funktion, alltså utan namn
def my_lambda(a, b):
    return a + b


# print(my_lambda(1, 2))

# first_function(lambda a, b: a+b)

people = [{"name": "Gian", "age": 30},
          {"name": "Kalle", "age": 45},
          {"name": "Gurra", "age": 12}]

# print(sorted(people, key=lambda person: person['age']))


def compare_name(person):
    return person["name"]


# print(sorted(people, key=compare_name))
def func_two(func: callable):
    def wrapper():
        func()
        print("func 2")
    return wrapper


@func_two
def func_one():
     print("func 1")


def func_three():
     print("func 3")


func_three = func_two(func_three)

func_one()
print("_____________")
func_three()