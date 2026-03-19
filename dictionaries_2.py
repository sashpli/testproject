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

