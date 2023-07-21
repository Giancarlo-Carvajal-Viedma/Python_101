# Först i en fil ska importen ligga.
import random
import enum

# Globala variabler
global x
x = 100

# Funktioner


# main
def main():
    print("My program")
    result = my_function()
    print(result)


# Hjälpfunktioner
def my_function():
    #Först ska variabler ligga.
    global x
    # Sen logik
    res = x+1

    # Sist return # return kan finnas i olika ställen
    return res


main ()