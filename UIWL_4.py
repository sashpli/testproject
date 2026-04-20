# parrot.py
# message = input("Tell me something and I will repeat it back to you: ")
# print(message)
#
# #greeter.py
# name = input("Please enter you name: ")
# print(f"Hello {name.title()}!")
#
# prompt = "If you tell us who you are, we can peronalize the message you see. "
# prompt += "\nWhat is you first name? "
# name = input(prompt)
# print(f"Hello {name}")

# accepting numerical input
# age = input("How old are you? ")
# age = int(age)

# heigt = input("How tall are you? ")
# heigt = int(heigt)
#
# if heigt >= 36:
#     print("You are tall enought to ride")
# else:
#     print("You are short to ride")

7-1
#--------------------------------------------------------------------------------
# Rental Car
# prompt = "What car do you want? "
# car = input(prompt)
# print(f"Let me see if i can get you a {car}!")
#
# prompt = input("What car do you want? ")
# print(f"Let me see if i can get you a {prompt}!")

# message = "How many people are in your dinner group? "
# people = input(message)
# people = int(people)
# if people >= 8:
#     print("Unfortunately you would have to wait for you tabel to be ready!")
# else:
#     print("Your table is ready!")
#
# message = input("How many people are in you dinner group? ")
# people = int(message)
# if people >= 8:
#     print("Unfortunately you would have to wait for you tabel to be ready!")
# else:
#     print("Your table is ready!")

prompt = input("Write a number! ")
number = int(prompt)
if number % 10 == 0:
    print("That's a multiple of 10!")
else:
    print("That's NOT a multiple of 10!")