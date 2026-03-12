alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print(f"You earned {str(new_points)} points!")

print("\n")

alien_0 = {'color': 'green', 'points': 5}  #adding items to an already existing dictionary
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {} #starting with an empty list and adding items
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

print("\n")
#Modifying Values in a Dictionary

alien_0 = {'color': 'green'}
print(f"the alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"the alien is now {alien_0['color']}.")
alien_0['type'] = 'angry'
print(f"the alien is {alien_0['type']} and has the color {alien_0['color']}.")
alien_0['type'] = 'calm'
print(f"the alien is {alien_0['type']} and has the color {alien_0['color']}.")


