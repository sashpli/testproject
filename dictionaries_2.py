# alien.py

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You now have {new_points} points.")

alien_0['x_position'] = 0

alien_0 = {'x_position': 0, 'speed': 'medium'}
if alien_0['speed'] == 'slow':
    x_incriment = 1
elif alien_0['speed'] == 'medium':
    x_incriment = 2
else:
    x_incriment = 3
alien_0['x_position'] = alien_0['x_position'] + x_incriment
print(f"You now moved {alien_0['x_position']}.")




print("\n")
# 6-1. Person
persons = {'first_name': 'max', 'last_name': 'power', 'city': 'chicago', 'age': 40}
print(persons['first_name'])
print(persons['last_name'])
print(persons['city'])
print(persons['age'])
print("\n")

# 6-2. Favorite Number
favorite_numbers = {
    'max': 5,
    'john': 9,
    'tom': 7,
    'bob': 17,
    'jeff': 99,
}
print(favorite_numbers['max'])
print(favorite_numbers['john'])
print(favorite_numbers['tom'])
print(favorite_numbers['bob'])
print(favorite_numbers['jeff'])

print("\n")

# 6-3. Glossary

glossary = {
    'print': 'Prints the statement.',
    'dictionary': 'Can store all kinds of data.',
    'loops': 'Python goes through all values in a list or dictionary.',
    'lists': 'Lists can store different data types.',
    'python': 'Is a programming language.',
}
print("Print:")
print(f"\t{glossary['print']}")
print("\nDictionary:")
print(f"\t{glossary['dictionary']}")
print("\nLoops:")
print(f"\t{glossary['loops']}")
print("\nLists:")
print(f"\t{glossary['lists']}")
print("\nPython:")
print(f"\t{glossary['python']}")

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for k, v in user_0.items():
    print(f"Key: {k}")
    print(f"Value: {v}")


print("\n")

# 6-4 Glossary 2

glossary = {
    'print': 'Prints the statement.',
    'dictionary': 'Can store all kinds of data.',
    'loops': 'Python goes through all values in a list or dictionary.',
    'lists': 'Lists can store different data types.',
    'python': 'Is a programming language.',
    }
glossary['test'] = 'this is  test'
glossary['test2'] = 'this is  test2'
glossary['test3'] = 'this is  test3'
glossary['test4'] = 'this is  test4'
glossary['test5'] = 'this is  test5'

for keys, values in glossary.items():
    print(f"Key: {keys}")
    print(f"Value: {values}")

# 6-5 Rivers
rivers = {'nile': 'egypt',
          'amazonas': 'brasil',
          'danube': 'austria'
          }
for river, country in rivers.items():
    print(f"The {river.title()} runs trough {country.title()}.")
for river in rivers:
    print(river.title())
#this one is the same as the above one
for river in rivers.keys(): #use .keys() for better readability
    print(river.title())
for river in rivers.values():
    print(river.title())

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
friends = ['jen', 'edward', 'sarah', 'jeff', 'george']
for name in friends:
    if name in favorite_languages.keys():
        print(f"{name.title()} thank you for taking the poll")
    else:
        print(f"{name.title()} take the poll")


