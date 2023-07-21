#lesson2, Jan 4, 2023
print("")
print("______________LIST/STRING_______________")
list1 = list() #skapar en variabel nämnd list1 som är tomt
list2 = list([1, "hello", True, None]) # denna lista har attributes, elements
list3 = []
list4 = [2, "world", False, 2, 2, 2, 2, "world", False, False,]
list5 = [2, "world", False, []] #Samma som lista 4 fast med array [], denna lista skapades för att list4 används längre ner för dict demonstration
list6 = [list2,list4] # En lista med två olika listor inuti
list7 = list2.copy() # Kopiera en lista

print (list1) 
print (list2)
print (list3)
print (list4)
print (list6)
print (list7)
list7.append("Fiskmås") # Ändrar du en lista inuti en annan lista så för båda inputen
print(hex(id(list2))) # Hitta addres
print(hex(id(list7))) # Har samma adress, tills vi ändrade med command .copy() på lista2

print (list2[1] + " " + list4[1] ) # print hello word med tomrum mellan orden, samt väljer element från listan

length = len(list2) # skapa variabel som räknar hur många elements listan 2 har i sig, dvs 4 (1,hello,true,none)
print(length) 

print(list2[len(list2)-1]) # denna räknar och printar ut specifik 1 element i listan
print(list2[-1])

string = "Gian" # likt listan fast allt i strängen räknas som en element
string_length = len(string) # räkna hur många bokstäver" strängen har, gian = 4

print(string_length)

print (string[0]) # printa ut första bokstaven av strängen "G"

list2[-1] = string #listor är mutible, går att ändras
print (list2)

# Funkar inte då strängar är immutible
# string[2] = "d"
# print(string)


sliced_list2 = list2[1:3] # välja printa ut specifika element inuti listan 1-3 alltså 0,hello,true,3
print(sliced_list2)

sliced_string = string[1:3] # välja printa ut specifik element inuti strängen 1-3: 0ia3
print (sliced_string)

list1.append(["hello, world!","hello, world again!"]) # .append: lägga till = denna lägger till i listan 1 som redan är skapad
list1.append("printa ut denna på samma lista också") # går att använda flera gånger, dock ej vanligt
print(list1)

list1.insert(1, "my") # lägga till i lista 1 på position 1
print(list1)

# set
print("")
print("______________SET_______________")

set1 = {1, 2, 3, 4} # innehåller unika värden
set2 = {} # om settet lämnas tomt blir det en dictionary, en dict
set3 = set() # annan typsätt för att undkomma att settet blir en dict
set4 = set(list4) # först fick vi fel för det fanns en array i settet, det funkar inte då, alltså "[]" i list4, det togs bort och då gick det


print(set1, type(set1))
print(set2, type(set2))
print(set3, type(set3)) # settet kan ej slice_
print(set4, type(set4)) # settet visar endast unika värden, kolla på list4, där finns flera upprepade värden.

print(set4.pop()) #commando .pop() tar bort en plats 
print(set4.pop()) 
print(set4.pop()) # här blir listan 4 tomt "den hade 3 unika värden" 

#Tuple
print ("")
print ("___________Tuple_____________")
tuple1 = () # Tuple funkar på samma sätt som set
tuple2 = tuple()
tuple3 = (1,2,3,"hello","world",False)
tuple4 = tuple((4,5,6,"Goodbye","Hell",True))

print(tuple1)  
print(tuple2)
print(tuple3)
print(tuple4) # Tuple går att unpack

a, b, c, d, e, f = tuple3 # Tuple går att unpack, men då måste alla unpackas
print(d, e) # värden går att unpacka, men inte ändras på samma sätt som set

# Dict/Dictionary
# Keys, Values, som object på Java. 
print("")
print("___________DICTIONARIES/DICT______________")

dict1 = {} # skapa tom dictionary
dict2 = dict() # nyckelord dict = dictionary
dict3 = {"name": "Gian", "age": 30} # keys är oftast strängar, men kan också vara värde; key=name,value=30
dict4 = ({"name": "Björne", "age": 50, (1, 2, 3): "korv", 1: "Bröd"}) # dicts är mutiable, går alltså att ändras senare, addas, bytas; 
# dict kan även innehålla tuples(1, 2, 3), tuples, numer, float, strings är immutible

print (dict3)
print (dict4)

print(dict3["name"]) # Select an element, key or value in dict
print(dict4.get("name")) # 

#print(dict3["fisk"]) # Funkar inte, fås error, då den ej finns med i dict
print(dict4.get("fisk")) # Går att skriva och kommer att printa ut men det står då "None"

print(dict4.get((1, 2, 3)))
print(dict4.get(1))

dict3["nationality"] = "COLOMBIAN" # Adds an item(element,value,key)

print(dict3)

pet_dict1 = {"name":"shirokumakum", "color": "white"}
pet_dict2 = {"name":"Biffen", "color": "Brown"}

company = {"name": "Mujina", "logo": "url", "employee": {"name": "Erik"}}

print(pet_dict1, pet_dict2)

dict3 ["pets"] = [pet_dict1, pet_dict2] # Vi kan ha en dict som är en lista

print(dict3)

dict3["company"] = company

print(dict3) # Hela dict
print(dict3["company"]) # Printa ut specifik lista inuti dict
print(dict3["pets"])

dict5 = dict4.copy()
print(dict4)
print(dict5)

dict5["name"] = "Sven"
print(dict4)
print(dict5)

print(hex(id(dict4)))
print(hex(id(dict5)))

dict_keys = dict5.keys()
dict_values = dict5.values()

print(dict_keys)
print(dict_values)