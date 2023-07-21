#Lesson 2, Jan 4, 2023
#Operatorer 
#Andra språk:  #//(och/eller) #&&(och) # == (lika med) # !=(inte lika med)
#Pyhon:        #or(och/eller) #and(och)                # not (inte lika med)
Gian ={"name": "Giancarlo", "age": 30, "description": "developer"}
name = "Giancarlo"

truth = name == "Gian" #operatorer returnerar alltid en boolean (True/False)

print(truth)

truth = Gian["age"] > 30
print(truth)

truth = Gian["age"] >= 30
print(truth)

truth = Gian["age"] < 30
print(truth)

truth = Gian["age"] <= 30
print(truth)

truth = Gian["age"] <= 30 and Gian["name"] == "Giancarlo" # Båda måste uppfyllas
print(truth)

truth = Gian["age"] <= 30 or Gian["name"] == "Giancarlo" # Ett vilkor måste uppfylas
print(truth)

truth = Gian["age"] <= 30 or not Gian["name"] == "Giancarlo"
print(truth)

truth = Gian["age"] <= 30 and not Gian["name"] == "Giancarlo"
print(truth)

truth = Gian["age"] <= 30 and not Gian["name"] != "Giancarlo"
print(truth)

#If

if True:
    print("Its the truth and nothin but the truth")

if Gian["name"] == "Giancarlo":
    print("What an impostor")

elif Gian["name"] == "Gian":
    print("its the truth")

elif Gian["age"]> 20:
    print("This him")

else:
    print("Something else ")

a_zero = 0
a_one = 1
a_none = None
an_empty_string = ""
a_string = " "

if not a_zero: # Noll blir ett false värde
    print("Zero is true")

if a_one: # Positiva och negativa siffror får true
    print("One is true")

if not a_none: # None evalueras till false då det är ingenting
    print("None is true")

if not an_empty_string: # tom sträng blir false
    print("String is true")

if a_string: # Bara ett tecken i en sträng gör att den blir true även om det är ett blanksteg.
    print("String is true")

