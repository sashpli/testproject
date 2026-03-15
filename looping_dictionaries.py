# Before we explore the different approaches to looping, let’s consider a
# new dictionary designed to store information about a user on a website.
# The following dictionary would store one person’s username, first name,
# and last name:
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

fav_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name, language in fav_lang.items(): #name und language sind key und value
    print(f"Name: {name.title()}"
          f"\nLanguage: {language.title()}\n")
    print(f"{name.title()}'s favorite language is {language.title()}")

fav_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name, language in fav_lang.items(): #name und language sind key und value
    print(f"{name.title()}'s favorite language is {language.title()}.")

# looping through all keys in a dictionary
fav_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in fav_lang.keys(): # keys() loops only the keys
    print(name.title())
for lang in fav_lang.values(): # values() loops only the values
    print(lang.title())

fav_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
friends = ['phil', 'sarah']
for name in fav_lang.keys():
    print(name.title())

    if name in friends:
        print(f"Hi {name.title()}, I see your favorite language is {fav_lang[name].title()}!\n")

# find out if a particular person was in the list
fav_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
if 'erin' not in fav_lang.keys():
    print("Erin, please take our poll!")

# looping through dictionary keys in order
fav_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in sorted(fav_lang.keys()):
    print(name.title() + ", thank you for making a poll")

# looping through values
fav_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("the following languages have been mentioned")
for language in fav_lang.values():
    print(language.title())

# unsing set for unique values and not repeating values that are double
fav_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("The following languages have been mentioned")
for language in set(fav_lang.values()):
    print(language.title())

# Glossary 2
glossary = {'string': 'A string is a text',
            'integer': 'An integer is a whole number',
            'if statement': 'An if statement checks if condition is true',
            'boolean': 'A boolean is a value that can only be true or false',
            'dictionary': 'A dictionary stores information in key-value pairs',
            'python': 'A progamming language',
            'set': 'I used by looping the list and dont get double elements'
            }
for keys, values in glossary.items():
    print(f'\nWhat does "{keys}" mean?')
    print(values)

print("\n")
#rivers
rivers = {'nile': 'egypt',
          'euphrat': 'iraq',
          'tigris': 'iraq',
          'mississippi': 'USA',
          'amazonas': 'brasil'}
for river, country in rivers.items():
    if country == 'USA':
        print(f"{river.title()} runs through the {country}")
    elif country != 'USA':
        print(f"{river.title()} runs through {country.title()}")
for river in rivers.keys():
    print(river)
for country in rivers.values():
    print(country)
#polling
fav_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
persons = ['jen', 'sarah', 'max', 'phil', 'john}']
for person in persons:
    if person in fav_lang.keys():
        print(f"{person.title()} thank you for taking the poll")
    else:
        print(f"{person.title()} please take the favorite language poll")