# User input input() function
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print(f"Hello, {name}!")

prompt = "if you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"Hello {name.title()}")

age = input("How old are you? ")
age = int(age)
print(f"You are {age} years old.")

heigt = input("How tall are you in inches? ")
heigt = int(heigt)
if heigt >= 36:
    print("You are tall enough to ride!")
else:
    print("You are to short for a ride!")

number = input("Please enter a number: ")
number = int(number)
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")