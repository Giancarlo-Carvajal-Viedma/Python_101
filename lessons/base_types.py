# lesson2, Jan 4,2023
# Grundläggande datatyperna

print ("")
print ("_____________Datatyper___________")
a_whole_number: int = 25 # hela numer
a_floating_point_number: float = 2.5 # decimal
a_string: str = "gian´s, world!" # längre sträng
a_boolean: bool = True #TRUE or FALSE, binär, 1 och 0
a_whole_lotta_a_nothin: None = None

print(f"Integer: {a_whole_number} - Type:{type(a_whole_number)}")
print(f"Float: {a_floating_point_number} - Type:{type(a_floating_point_number)}")
print(f"String: {a_string} - Type:{type(a_string)}")
print(f"Boolean: {a_boolean} - Type:{type(a_boolean)}")
print(f"None: {a_whole_lotta_a_nothin} - Type:{type(a_whole_lotta_a_nothin)}")



#Aritmetik/Beräkning
# INT
# En int vid operationer addition, subtration, multiplikation
#En operation dör andra talet är en float blir en float och även division mellan 2 integers blir en float 
print ("")
print ("_____________INT___________")

int1 = 10
int2 = 5
test_float = 2.5

int3 = int1 + int2
print(int3, type(int3))

int3 = int2 - int1
print(int3, type(int3))

int3 = int1 * int2
print(int3, type(int3))

int3 = int1 / int2
print(int3, type(int3))

int3 = int1 + test_float
print(int3, type(int3))

# Float
# All aritmetik med en float resulterar med en float
print ("")
print ("_____________FLOAT___________")

float1 = 2.0
float2 = 1.5

float3 = float1 + float2
print(float3, type(float3))

float3 = float2 - float1
print(float3, type(float3))

float3 = float1 * float2
print(float3, type(float3))

float3 = float1 / float2
print(float3, type(float3))

float3 = int1 + float1
print(float3, type(float3))

# String
print ("")
print ("_____________STRING___________")

string1 = "Gian"
string2 = "Hej"

string3 = string1 + string2
print(string3, type(string3))

# Funkar inte
# string3 = string2 - string1
# print(string3, type(string3))

# Funkar inte
# string3 = string1 * string2
# print(string3, type(string3))

string3 = string1 * int1
print(string3, type(string3))

# Funkar inte
# string3 = string1 / string2
# print(string3, type(string3))

# Funkar inte
# string3 = int1 + string1
# print(string3, type(string3))

# Funkar inte
# string3 = float1 + string1
# print(string3, type(string3))

# BooleanS
print ("")
print ("_____________BOOLEAN___________")

bool1 = True # binär (1)
bool2 = False # binär (0)

bool3 = bool1 + bool2
print(bool3, type(bool3))

bool3 = bool2 - bool1
print(bool3, type(bool3))

bool3 = bool1 * bool2
print(bool3, type(bool3))

# Funkar inte eftersom det är division med 0
# bool3 = bool1 / bool2
# print(bool3, type(bool3))

bool3 = bool2 / bool1
print(bool3, type(bool3))

bool3 = int1 + bool1 # int1=10 bool1 = 1 -> 10+1
print(bool3, type(bool3))

bool3 = float1 + bool1 # float1=2.0 bool1=1 -> 2.0+1=3.0
print(bool3, type(bool3))

# None
# None, lite speciellt, funkar inte med all aritmetik, inga operationer
print ("")
print ("_____________NONE___________")

none1 = None
print('"Kan ej genomföra aritmetiska operationer med None"')
# Funkar inte, inte ens addition
# test = int1 + none1
# print(test, type(test))

# Casting

print("")
print("___________CASTING___________")

floater = 1.0
inter = 1
inter2 = 0
stringer = "1"
stringer2 = "1.5"
booler = True
booler2 = False

print(int(floater))
print(float(inter))
print(int(stringer))
# print(int(stringer2))
print(float(stringer))
print(float(stringer2))

print(bool(inter))
print(bool(inter2))

print(int(booler))
print(int(booler2))

print(float(booler))
print(float(booler2))

print(str(floater))
print(str(inter))
print(str(booler))