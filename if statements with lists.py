from zoneinfo import available_timezones

requested_toppings = ['mushrooms' , 'green peppers' , 'extra cheese']
for requested_topping in requested_toppings:  #Achtung!!! Unterschied requested_topping in requested_toppings (s!)
    print(f"Adding {requested_topping} to your pizza")
print("Finished making your pizza!")

print("\n")

requested_toppings = ['mushrooms' , 'green peppers' , 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print(f"Sorry we are out of {requested_topping}!")
    else:
        print(f"{requested_topping.title()} added to your pizza")
print("Finished making your pizza!")

print("\n")


requested_toppings = []
#starting with if statement when name of list is used in Python, it returns TRUE
#if the list contains one item. Empty list is False, if toppings passes test then run for loop
#if test FALSE then print ELSE statement
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping} to your pizza")
    print("Finished making your pizza!")
else:
        print("Are you sure you want a plain pizza?")

print("\n")
#Using multiple Lists

available_toppings = ['mushrooms' , 'olives' , 'grenn peppers'
                    'pepperoni' , 'pineeapple' , 'extra cheese']
requested_toppings = ['mushrooms' , 'frensh fries' , 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping} to your pizza")
    else:
        print(f"Sorry, we don't have {requested_topping}!")
print("Finished making your pizza!")

#Das ist eine Dictonary wo man den preis direkt mit einem string verknüfen kann mit einer {}
print("\n")
available_options = {'carbon wheels' : 1000 , 'spoiler' : 200, 'color change' : 2000, 'stripes' : 4000, 'new springs' : 5000}
requested_options = ['carbon wheels' , 'spoiler' , 'tinted windows' , 'new springs']
for requested_option in requested_options:
    if requested_option in available_options:
        price = available_options[requested_option]
        print(f"Adding {requested_option} which costs ${price} to your car")
    else:
        print(f"Sorry, we don't do {requested_option} here!")
print("Finished tuning your car")