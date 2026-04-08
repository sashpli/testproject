# # parrot.py
# # user in put while loops
# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)
#
# # greter.py
# name = input("Please enter your name: ")
# print(f"Hello {name}, welcome to python!")
#
# message = "if you tell us who you are, we can personalize the message you see."
# message += "\nWhat is your first name? "
# name = input(message)
# print(f"Hello {name.title()}, welcome to pycharm!")
#
# # using int for numerical input
#
# heigth = input("How tall are you? ")
# heigth = int(heigth)
# if heigth >= 36:
#     print("You are tall enought to ride")
# else:
#     print("You are to short to ride")
#
# # even or odd
# number = input("Enter a number, and Ill tell you if its even or odd: ")
# number = int(number)
# if number % 2 == 0:
#     print(f"{number} is even")
# else:
#     print(f"{number} is odd")
#
#
# # rental car
# message = "What kind of rental car do you want? "
# message = input(message)
# print(f"Let me find you a {message}")
#
# # prompt = input("What kind of car do you want? ")
# # print(f"{prompt} is a nice car!")
#
#
# # restaurant seating
# message = input("How many people are in you dinner group? ")
# message = int(message)
# if message >= 8:
#     print("I am sorry you will have to wait")
# else:
#     print("Your table is ready")
#
#
# # version 1
# message = "What kind of rental car do you want? "
# message = input(message)
# print(f"Let me see if I can get you a {message}")
#
# # version 2
# message = input("What kind of car do you want to rent2? ")
# print(f"Let me see if I can get you a {message}")
#
#
#
#
# prompt = "How many people are in you group? "
# prompt = input(prompt)
# if int(prompt) > 8:
#     print("Sorry but you have to weit")
# else:
#     print("Your table is ready")
#
# # asking if its a multiple of 10
# prompt = "Write a number and I will tell you if it is a multiple of 10 or not: "
# prompt = input(prompt)
# if int(prompt) % 10 == 0:
#     print("its a multiple of 10")
# else:
#     print("not a multiple of 10")


# __________________________________________________________________
# A WHILE LOOP RUNS AS LONG AS A CERTAIN CONDITION IS " T R U E "

# counting
current_number = 1
while current_number <= 5:  # runs as long as its less than or equal 5 !
    print(current_number)
    current_number += 1  #add 1 after every while loop as long as its less than or equal 5

# letting the user choose when to quit
prompt = "\nTell me something and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program"
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)