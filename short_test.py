alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original x_position: {alien_0['x_position']}")
if alien_0['speed'] == 'slow':
    x_incriment = 1
elif alien_0['speed'] == 'medium':
    x_incriment = 2
else:
    x_incriment = 3
alien_0['x_position'] = alien_0['x_position'] + x_incriment
print(f"The new positon is {alien_0['x_position']}")

# removing key value pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['color']
print(alien_0)

fav_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name, language in fav_lang.items(): #name und language sind key und value
    print(f"Name: {name.title()}\nLanguage: {language.title()}\n")

rivers = {'nile': 'egypt',
          'euphrat': 'iraq',
          'tigris': 'iraq',
          'mississippi': 'USA',
          'amazonas': 'brasil'}

if rivers.values() == 'USA':
    print(f"{river.title()} runs through {place}")
