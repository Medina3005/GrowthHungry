# Strings and Operations:
# - Basic String Operations
# - String Slices
# - String Formatting
# Project:
# Complete the string1.py exercise in the provided python_exercises folder. Try string_2 too, if you're curious.


# mystring = "Hello World"
# mystring2 = 'Hello World'


# mystring = "Hello World!"
# print("single quotes are ' '")
# print(len(mystring))


# mystring = "Alina loves reading a books!"
# print(mystring.index("l"))

# mystring  = "John Snow"
# print(mystring.count("n"))         # will count how many same letters do u have. for example n - it will give 2 or if u put another letter that don't have in that string, it will print 0


# mystring = "John Snow!"
# print(mystring[4:7]) #splice it also counts as number starts from 0,1,2,3,4....


# mystring = "John Snow!"
# print(mystring[4::2]) # step- how many steps to make if 1 - means one by one, if 2 means it will lw

# mystring = "John Snow!"
# print(mystring[-3::])  # left to right will print all numbers

# mystring = "John Snow!"
# print(mystring[-3:-5:-1]) 

# # Upper / Lower Case 

# mystring = "John Snow!"
# print(mystring.upper())   # will print all words in Upper case A
# print(mystring.lower())   # will print all words in Lower case a


# mystring = "John Snow"
# print(mystring.startswith("John")) # will print true if it starts with John
# print(mystring.endswith("Alina")) # prints false if last words doesn't starts with Alina


# mystring = "Hello, my name is Medina"
# mystring = mystring.split("e")                    #split can ['Hello, my name is Medina']
# print(mystring)

# String Formatting 

# name = "Medina"
# name = name + " new stuff"
# print("Hello, %s!" % name)  # %s - string variable 



# name = "Medina"
# age = 20
# print("%s is %d years old." % (name, age)) # %d works with number u'r gonna put

# name = "Amantur"
# coworker = 21
# print("%s is dating with Aigerim, but likes Medina, who's %d years old." % (name, coworker))


# name = "Amantur"
# name1 = "Aziza"
# coworker = 21
# coworker1 = 23
# print("%s is dating with Aigerim,  but likes Medina, who's %d years old. and %s  is %d years old" % (name, coworker, name1, coworker1))  
# # so you can put those initials, and print step by step. 


# mylist = [30, 50, 40]
# print("My school score is: %s" % (mylist))
#My school score is: [30, 50, 40] - > output will give as a number without square brackets. 

# Specifiers

# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot. 

# %x/%X - Integers in hex representation (lowercase/uppercase)

# %x / %X — shows integers in hexadecimal (base-16) form. 


# data = ("Medina", "Alina", 55.65)
# format_string = "Good Afternoon"
# print(format_string % data)


number = 255
print("%x" % number)  # lowercase hex
print("%X" % number)  # uppercase hex