my_list = []

my_list.append("Gian")

my_list.append("Carlo")

my_list.reverse()

my_list.clear()

my_list.append("Gian")

my_list.append("Carlo")

count = my_list.count("Korv")

element = my_list.pop()

my_list.append("GC")
my_list.append("Anna")
my_list.append("Alexandersson")

# Vi kan inte jämföra strängar med siffror så det mpste vara samma datatyp i listan. 
# my_list.append(1)
# my_list.append(True)

my_list.sort(reverse = True)

# print(my_list, count, element)

list2 = [1, 10, 43, 4, True, False]

list2.sort()

# print(list2)

my_string = "Hej jag heter Gian"
# print(my_string)
my_string_list = list(my_string)
# print(my_string_list)

my_split_string = my_string.split('h')

# print(my_split_string)

my_email = "gian@smart.se"

# Detta är samma som nedan
my_domain = my_email.split('@')[1].split('.')[0]
# print(my_domain)

# split_string = my_email.split('@')
# print(split_string)
# domain = split_string[1]
# print(domain)
# split_domain = domain.split('.')
# print(split_domain)
# company = split_domain[0]
# print(company)

my_untrimmed_string = "         Gian        "
# print(my_untrimmed_string)
my_trimmed_String = my_untrimmed_string.strip()
# print(my_trimmed_String)

letter_list = ["G", "I", "A", "N"]

my_name = "".join(letter_list)
print(my_name)

# funkar inte, listor har ingen .join
# my_name_again = letter_list.join()
# print(my_name_again)
