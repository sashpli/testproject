age = 19
if age >= 18:
    print(f"With {age} years old, you are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print(f"Sorry, you are too young to vote!")
    print("Please register to vote as soon as you turn 18")

#if elif else
age = 17
if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $5")
else:
    print("Your admission cost is $10")
print("\n")

age = 20
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")

age = 66
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("Your admission cost is $" + str(price) + ".")

age = 54
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("Your admission cost is $" + str(price) + ".\n")

requested_toppings = ['mushrooms' , 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
print("\nFinished making your pizza!")

gehalt = 2001
if gehalt == 2000:
    print('Ihr Gehalt is genau richtig')
elif gehalt <= 1999:
    print('Ihr Gehalt is zu niedrig')
elif gehalt >= 2001:
    print('Ihr Gehalt ist hoch')



