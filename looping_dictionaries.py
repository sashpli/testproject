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

