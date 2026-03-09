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

