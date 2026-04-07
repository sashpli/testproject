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




































# rental car
message = "What kind of rental car do you want? "
message = input(message)
print(f"Let me find you a {message}")

# prompt = input("What kind of car do you want? ")
# print(f"{prompt} is a nice car!")


# restaurant seating
message = input("How many people are in you dinner group? ")
message = int(message)
if message >= 8:
    print("I am sorry you will have to wait")
else:
    print("Your table is ready")