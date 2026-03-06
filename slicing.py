#slicing lists

players = ['chales' , 'martina' , 'michael' , 'florence' , 'eli']
print(players[0:3])
print(players[-3:])

print(f"Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

my_foods = ['pizza' , 'falafel' , 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friends favorite foods are:")
print(friend_foods)

print("\n")

print("The first three items in the list are:")
print(players[:3])

print("The items from the middle of the list are:")
print(players[1:3])

print("The last three items in the list are:")
print(players[-3:])

pizzas = ['margerita' , 'salami' , 'capriciosa']
friend_pizzas = pizzas[:]
pizzas.append('napoli')
friend_pizzas.append('quattro formaggi')
#print("My friends pizzas are:")
#for favpizza in pizzas:
    #print(favpizza.title())
#print("\n")
#print('My friends favorite pizzas are:')
#for friendfavpizza in friend_pizzas:
    #print(friendfavpizza.title())
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("\nMy friends pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

