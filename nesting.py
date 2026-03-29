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


# 6-7 People

person_1 = {'first': 'max', 'last': 'smith', 'age': 30, 'city': 'miami'}
person_2 = {'first': 'john', 'last': 'bauer', 'age': 40, 'city': 'london'}
person_3 = {'first': 'bob', 'last': 'schneider', 'age': 50, 'city': 'berlin'}
persons = [person_1, person_2, person_3]
for person in persons:
    print(f"His name is {person['first'].title()} {person['last'].title()}, he is {person['age']} years old and lives in {person['city'].title()}.")
    print(f"First Name: {person['first'].title()}")
    print(f"Last Name: {person['last'].title()}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city'].title()}")


# 6-9 Pets
tom = {'owner': 'john', 'type': 'cat'}
jerry = {'owner': 'bob', 'type': 'mouse'}
teddy = {'owner': 'george', 'type': 'bear'}
pets = [tom, jerry, teddy]
for pet in pets:
    print(f"The owners name is {pet['owner'].title()} and the pet is a {pet['type']}.")




# 6-9 Favorite Places - three names as keys and one of three favorite places for each person
favorite_places = {
    'john':{'fav_place_1': 'london',
            'fav_place_2': 'tokyo',
            'fav_place_3': 'denver',},
    'ted': {'fav_place_1': 'paris',},
    'jerry': {'fav_place_1': 'new york',
              'fav_place_2': 'chicago',
              'fav_place_3': 'boston',},
    'adam': {'fav_place_1': 'berlin',
             'fav_place_2': 'sacramento',}
}
for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for rank, place in places.items():
        print(f"{place.title()}")
print('\n')

# 6-10 Favorite Numbers
favorite_numbers = {
    'max': {'num_1': 5, 'num_2': 99, 'num_3': 65},
    'john': {'num_1': 9},
    'tom': {'num_1': 7, 'num_2': 19, 'num_3': 87, 'num_4': 4},
    'bob': {'num_1': 17, 'num_2': 0},
    'jeff': {'num_1': 9, 'num_2': 2, 'num_3': 38, 'num_4': 32, 'num_5': 5},
}
for name, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        for favnumb, number in numbers.items():
            print(f"{name.title()}'s favorite number is: \n{number}")
    else:
        print(f"{name.title()}'s favorite numbers are:")
        for favnumb, number in numbers.items():
            print(number)


print('\n')
# 6-11 Cities

cities = {'london': {'country': 'united kingdome',
                     'populations': 9.1,
                     'fact': 'It was founded by the romans'},
          'new york': {'country': 'united states',
                       'populations': 8.6,
                       'fact': "It's first name was New Amsterdam"},
          'tokyo': {'country': 'united kingdome',
                    'populations': 41,
                    'fact': 'It is the worlds most populated city'},
}
for name, cities in cities.items():
    print(f"{name.title()} has a population of about {cities['populations']} million people."
          f" A fun fact about {name.title()}is: {cities['fact']}")























































