# Data Types and Basic Operations:
# - Data types: Strings (text), Numbers (Integers (whole numbers), and Floats (decimal numbers)).
# - Variables (storing data like text and numbers).
# - Arithmetic operators (+, -, *, /, % for remainder), type conversion (e.g., turning a user's text input into a number).
# - Lists and Operations
# - Using input() to get user data and print() to display it.
# Project:
# Basic Tip Calculator. Write a program that asks for the total bill amount and the tip percentage. It should then calculate and
# display the tip amount and the total bill including the tip.
# Advanced: You can also ask for a name (using input()) and print the total amount with that name in it.
# Solve the problems in list1.py in the provided python_exercises folder that do not use sorting

# Integer and Floats 

# y = 7
# print(y) - > Integer 

# y = 7.5
# print(y) -> Float 


# x = 6.3
# x = 3 * x
# print(x)

# x = 7.5
# print(x)

# y = x 
# y = 2 * x
# print(y)

# Strings are defined with one quote or double quote 

# mystring = "Don't spend your time for boys"
# print(mystring)

# my_book_harry = 'pholosoph stone'
# print(my_book_harry)

# my_book_harry = "philosophe stone"
# print(my_book_harry)                            #Will always give the output from data

# print('print')
# print("print")            # will print as a variable


# five = 3
# four = 6
# one = five + four
# print(one)

# medina = "deep"
# career = "mind"
# deepmind = medina + ' ' + career
# print(deepmind)


# x = 7
# a = 30
# b = 3
# c = 2005

# a,b,c = 30,3,2005
# print(a,b,c)


# Arithmetic Operators 

# num = 1 + (2*10) / 4
# print(num)

# Modulo Operator

# remainder = 10 % 3              # -> will give 1 as an output 
# division = 10 / 3
# print(remainder)
# print(division)    



# any_number = 7 ** 6   -> using multiplication to get the power relationship ^2 
# square = 8 ** 2
# cube = 6 ** 3
# print(any_number)
# print(square)
# print(cube)


# Using Operators with Strings 

# johnsnow = "I" " "+ "Love" " "+ "movie"
# print(johnsnow)

# johnsnow = "I"
# book = "Love"
# output = "movie"
# print(johnsnow,book,output)


# class1 = "students\n" * 20
# print(class1)

# mystring = "hello"
# myfloat = 10.0
# myint = 20

# # testing code
# if mystring == "hello":
#     print("String: %s" % mystring)
# if isinstance(myfloat, float) and myfloat == 10.0:
#     print("Float: %f" % myfloat)
# if isinstance(myint, int) and myint == 20:
#     print("Integer: %d" % myint)


# List and Operators

# index starts from 0, 1, 2, 3

# colors = ['red', 'blue', 'green']
# print(colors[0])
# print(colors[2])
# print(len(colors))

# Append - adds a single element to the end of the list. Common error: doesn't return the new list, just modifies the original
# mylist = []
# mylist.append(8)
# mylist.append(4)
# mylist.append(7)
# # 0 1 2
# # [8,4,7]
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])

# mylist = [1,2,3]
# print(mylist[1])

# mylist = [1,2,3]
# mylist.append(4)
# print(mylist)
# # prints [1,2,3,4]

# mylist = [1,2,3]
# mylist.append(4)
# print(mylist[3])
# #prints out 4



# list.insert(index,elem) - inserts the element at the given index, shifting elements to the right. 

# mylist = ['larry', 'curly', 'moe']
# mylist.append('shemp')
# mylist.insert(3, 'book')
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[3])
# print(mylist[4])
# #prints book larry curly moe shemp


# list.extend(list2) -> adds the elements in list2 to the end of the list.
# Using + or += on a list is similar to using extend()

# mylist = ['larry', 'curly', 'moe']
# mylist.append('shemp')
# mylist.insert(1, 'book')

# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[3])
# print(mylist[4])

# mylist.extend(['here', 'something', 'il'])
# print(mylist)
# output ['larry', 'book', 'curly', 'moe', 'shemp', 'here', 'something', 'il']


# list.index(elem) - searches for the given element from the start of the list and returns its index. 
# Throws a ValueError if the lement doesn't appear(use "in" to check without a ValueError).

# mylist = ['larry', 'curly', 'moe']
# mylist.append('shemp')
# mylist.insert(1, 'book')

# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[3])
# print(mylist[4])

# mylist.extend(['here', 'something', 'il'])
# print(mylist)
# print(mylist.index('moe'))

#output will show 3 

# list.remove(elem) - searches for the first instance of the given element and removes it
# (Throws ValueError if not present)

# mylist = ['larry', 'curly', 'moe']
# mylist.append('shemp')
# mylist.insert(1, 'book')

# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[3])
# print(mylist[4])

# mylist.extend(['here', 'something', 'il'])   # how to define extend
# print(mylist)

# print(mylist.index('moe'))                    # how to define index

# mylist.remove('curly')                         # how to remove 
# print(mylist)

# list.sort() - sorts the list in place (does not return it). (The sorted() function shown later is preffered)


# mylist = ['larry', 'curly', 'moe']
# mylist.append('shemp')
# mylist.insert(1, 'book')

# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[3])
# print(mylist[4])

# mylist.extend(['here', 'something', 'il'])   # how to define extend
# print(mylist)

# print(mylist.index('moe'))                    # how to define index

# mylist.remove('curly')                         # how to remove 
# print(mylist)

# mylist.sort()
# print(mylist)                               # sort the words throght alpabetical 


# # list.reverse() - reverses the list in place(doesn't return it) 

# mylist = ['larry', 'curly', 'moe']
# mylist.append('shemp')
# mylist.insert(1, 'book')

# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[3])
# print(mylist[4])

# mylist.extend(['here', 'something', 'il'])   # how to define extend
# print(mylist)

# print(mylist.index('moe'))                    # how to define index

# mylist.remove('curly')                         # how to remove 
# print(mylist)

# mylist.sort()
# print(mylist)                               # sort the words throght alpabetical  A-Z

# mylist.reverse()
# print(mylist)                               # sort the words from alpabetical Z-A

# mylist.reverse()
# print(mylist)


# # list.pop(index) - removes and returns the element at the given index.
# # Returns the rightmost element if index is omitted (roughly the opposite of append())

# mylist = ['larry', 'curly', 'moe']
# mylist.append('shemp')
# mylist.insert(1, 'book')

# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[3])
# print(mylist[4])

# mylist.extend(['here', 'something', 'il'])   # how to define extend
# print(mylist)

# print(mylist.index('moe'))                    # how to define index

# mylist.remove('curly')                         # how to remove 
# print(mylist)

# mylist.sort()
# print(mylist)                               # sort the words throght alpabetical  A-Z

# mylist.reverse()
# print(mylist)                               # sort the words from alpabetical Z-A

# mylist.reverse()
# print(mylist)


# my_element = mylist.pop(0)
# print(my_element)
# print(mylist)

# # or 

# mylist.pop(2)
# print(mylist)         # we can put any index number that we want to remove for example 1 or 2 and using the pop will remove that mumber

# As I found the difference between remove and pop is that remove function delete only specific word when you write " jhdscbjhb"
# pop remove the index word. for example you put 3 and it will remove the word that defines as a index 3. 
# adding to this remove don't print the output after removing the word. 



# Input() - is a function that allows a program to receive data from the user though the keybord while the program is running 

# astring = input("print your name:")
# print(astring)


# num = int(input("Please enter your number:"))
# decimalnum = float(input("Please enter your decimal number:"))
# print(num % decimalnum)                                            


# a = 8
# b = 0.78
# c = "book"
# print("a is : %d, b is %0.4f, c is %s" % (a,b,c))                 #d means decimal number , .f - %0.4f - show number after duts. %s - show string 



# Project:
# Basic Tip Calculator. Write a program that asks for the total bill amount and the tip percentage. It should then calculate and
# display the tip amount and the total bill including the tip.
# Advanced: You can also ask for a name (using input()) and print the total amount with that name in it.
# Solve the problems in list1.py in the provided python_exercises folder that do not use sorting

name = input("Enter your name: ")
print(name)

total_amount = float(input("Enter total amount:"))
print(total_amount)
tip_percent = int(input("Please choose your tip %: "))
print(tip_percent)


tip = (total_amount * tip_percent) / 100
total_bill = total_amount + tip
total_bill = round(total_bill, 2)
print("Your total bill amount is:", total_bill, "with", str(tip_percent) + "%", "tip:", tip)



