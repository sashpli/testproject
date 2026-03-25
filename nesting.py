alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

print("\n")

# Make an empty list for storing aliens
aliens = []

# make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
#show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print('...')
#show how many aliens habe been created
print(f"Total number of aliens {len(aliens)}")

cars = []
for car_number in range(20):
    new_car = {'make': 'bmw', 'HP': 300, 'color': 'black'}
    cars.append(new_car)

for car in cars[:5]:
    if car['make'] == 'bmw':
        car['make'] = 'audi'
        car['HP'] = 150
        car['color'] = 'green'
for car in cars[:10]:
    print(car)

# nesting foods
foods = []

for new_foods in range(15):
    food = {'tye': 'banana', 'taste': 'sweet', 'color': 'yellow'}
    foods.append(food)

for food in foods[:5]:
    if food['tye'] == 'banana':
        food['taste'] = 'sour'
        food['color'] = 'green'
for food in foods[:10]:
    print(food)

# A List in a Dictionary pizza.py

# Store information about a pizza beeing ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'extra cheese'],
}
# summarize the order
print(f"You ordered {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print(topping)

# favorite languages.py
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print(f"\n {name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")


favorite_cars = {
    'john': ['alfa romeo', 'bwm', 'audi'],
    'tom': ['mercedes', 'toyota'],
    'jeff': ['ferrari', 'lamborghini'],
    'bob': ['ford'],
    'ted': ['porsche', 'jaguar']
}
# calling the KEYS and VALUES with .items()
for name, make in favorite_cars.items():
    if len(make) == 1:
        print(f"{name.title()}'s favorite car is:")
    else:
        print(f"{name.title()}'s favorite cars are:")
    for car in make:
        print(f"{car.title()}")

# A dictionary in a Dictionary
# many_users.py

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }
}
for username, userinfo in users.items():
    print(f"Username: {username}")
    full_name = userinfo['first'] + ' ' + userinfo['last']
    location = userinfo['location']
    print(f"\tFull Name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
