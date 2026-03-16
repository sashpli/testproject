# Sometimes you’ll want to store a set of dictionaries in a list or a list of
# items as a value in a dictionary. This is called nesting. You can nest a set
# of dictionaries inside a list, a list of items inside a dictionary, or even a
# dictionary inside another dictionary.
from ftplib import all_errors

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

print("\n")
# Make an empty list for storing aliens
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

#show the first 5 aliens:
for alien in aliens[:10]:
    print(alien)
print("...")

#show how many aliens have been created.
print(f"Total number of aliens {len(aliens)}")

# A List in a dictionary
#Liste in Dictionary — ein einzelnes Objekt hat unter einem Schlüssel mehrere Werte.
# Stell dir einen Kontakt vor: eine Person, aber mehrere Telefonnummern. Der Zugriff geht immer dict["schlüssel"][index].
# Dictionary in Liste — viele gleichartige Objekte werden gesammelt. Genau das macht dein Auto-Programm: 20 Autos, jedes mit denselben Schlüsseln (color, speed, price).
# Der Zugriff geht liste[index]["schlüssel"].
# Der entscheidende Unterschied ist also: was steht außen? Eine geschweifte Klammer { bedeutet Dictionary ist der Container, eine eckige [ bedeutet Liste ist der Container.

# Store information about a pizza being ordered
pizza = {'crust': 'thick',
         'toppings': ['mushrooms', 'extra cheese'],}
#summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza"
      f" with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping.title()}")

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    if len(languages) < 2:
        print(f"\n{name.title()}'speaks only one language that is {languages[0].title()}")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")

users = {
    'aeinsetin': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    }
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']

    print(f"Full Name: {full_name}")
    print(f"Location: {location}")