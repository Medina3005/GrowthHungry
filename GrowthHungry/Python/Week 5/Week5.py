# Repetitive Tasks with Loops:
# - For loop and using range()
# - While loop
# - Break and continue
# Project:
# Number Guessing Game. The program chooses a secret random number between 1 and 100. The user has a limited number of attempts to guess it.
# After each guess, the program tells the user if their guess was "too high," "too low," or "correct."
# Project:
# Simple To-Do List. Create a program that allows a user to manage a to-do list. The user should be able to: Add a new task. View all tasks. Delete a task by its name or number.
# The program should loop until the user decides to quit.


# LOOPS -> iterate one by one by the end

# primes = [2, 3, 5, 7]
# for prime in primes:
#     print(prime)
#     print("medina")
# x = 8
# print(x)


# for x in range(6):
#     print(x)

# for x in range(3,7):
#     print(x)

# for x in range(10,20,5):
#     print(x)


# WHILE LOOP
# conditions works only when they are true
# infinite loop

# count = 0
# while count < 5:
#     print(count)
#     count += 1
# print("white loop exited")


# BREAK AND CONTINUE STATEMENTS

# break is used to exit a for loop or a while loop, 
# whereas continue is used to skip the current block, and return to the "for"
# or "while" statement. 

# Example:

# count = 0
# while True:
#     print(count)
#     count += 1
#     # if count >= 5:
#     break 


# for x in range(10):
#     if x % 2 == 0:
#         continue # this iteration is neglected that's why it goes to next itertion
#     print(x)


for i in range(1,10):
    if(i%5==0):
        break
    print(i)
else:
    print("the code will not print after else:, because we can divide 5/5")

    