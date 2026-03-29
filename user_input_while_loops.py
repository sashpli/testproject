#message = input("Tell me something, and I will repeat it back to you: ")
#print(message)
from operator import truediv

# name = input("Please enter you name: ")
#print("Hello, " + name + "!")

# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += ("\nWhat is you first name?")
# name = input(prompt)
# print(f"Hello, {name}!")
# prompt = "If you tell us who you are, we can personlaize the message you see"
# prompt += "\nWhat is you name"
# name = input(prompt)
# print(f"Hello {name}!")
#
# age = input("How old are you?")
# age = int(age)
# age >= 18

# #height = input("How tall are you in inches? ")
# height = int(height)
# if height >= 36:
#     print(f"\nYou are tall enough to rinde")
# else:
#     print(f"\nYou'll be able to ride wehen you're a little older")

# # even or odd
# number = input("Enter a number and I will tell you if its even or odd: ")
# number = int(number)
# if number % 2 == 0:
#     print(f"\n{number} is an even number")
# else:
#     print(f"\n{number} is an odd number")

# 7-1 Rental Car
# cars = input("What rental car would you like? ")
# print(f"\nLet me see if I can get you a {cars.title()}.")
#
# people = input("How many people are in the dinner group? ")
# people = int(people)
# if people >= 8:
#     print("\nSorry, you'll have to wait for a table.")
# else:
#     print("\nYour table is ready")

# print("\n")
#
# # While Loop
#
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# Choosing when to quit

#
# prompt = "\nTell me something and I will reapeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
#
# message = ""
# while message != "quit":
#     message = input(prompt)
#     if message != "quit":
#         print(message)


# Flags

# prompt = "\nTell me something and I will reapeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
#
# active = True
# while active:
#     message = input(prompt)
#
#     if message == "quit":
#         active = False
#     else:
#         print(message)
#
#
# # Using a break
#
# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "
#
# while True:
#     city = input(prompt)
#     if city == "quit":
#         break
#     else:
#         print(f"I'd love to visite {city.title()}.")
#
# prompt = "\nWhat car do you drive? "
# prompt += "\n(Enter 'quit' when you are finished.) "
# while True:
#     car = input(prompt)
#     if car == "quit":
#         break
#     else:
#         print(f"Thats a nice {car.title()}.")
#

prompt = "\nWhat car do you drive? "
prompt += "\n(Enter 'quit' when you are finished.) "
prompt += "\n--> "

car = ""
active = True
while active:
    car = input(prompt)
    if car == "quit":
        active = False
    else:
        print(f"That's a nice a {car.title()}")

prompt = "\nWhat do you like to eat? "
food = ""
while food != "quit":
    food = input(prompt)
    print(f"{food.title()} tastes bad!")


