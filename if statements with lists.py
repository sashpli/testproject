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
