# lesson2, Jan 4, 2023
# Loops
my_list = ["Gian", "Carlo", "Apples", "Oranges"]
my_dict = {"name": "gian", "age":30,"description":"developer"}
print (my_list)

# For-loop # Fungerar så länge i>string(my_list)
for string in my_list: #for-loop; får alla element i listan: my_list
    print(string)

for a in range(5): #En loop som upprepas 4 gånger
    print(a)

for i in range(len(my_list)): #En loop som visar alla element i my_list
    print(my_list[i])

for i, string in enumerate(my_list): # i for index or integer # returnerar en tupple med numererat arrays
    print (i, string)

for key in my_dict.keys():
        print(key, my_dict[key])

for key,value in my_dict.items():
        print(key, value)

# while-loop ; loop är med false, true så kan den skapas
# Det som händer i while loop måste påverka evalueras
#infinite loop # DONT RUN!
#while True:
 #    print("True :D")
                            # Another way of writing the same:
number =1                   # number = 1
while True:                 # while number <= 42:
    number = number + 1     # number = number + 1
    if number ==1:          # print(number)
         continue                 
    print(number)                     
    if number > 10:         
     break