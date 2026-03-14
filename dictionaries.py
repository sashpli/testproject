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

#Modifying Values in a Dictionary

alien_0 = {'color': 'green'}
print(f"the alien is {alien_0['color']}.")
alien_0['color'] = 'red'
print(f"the alien is now {alien_0['color']}.")

#Position of an alien that can move at different speeds
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original x-position: {str(alien_0['x_position'])}.")
# Move the alien to the right
# Determine how far to move the alien based on its current speed
if alien_0['x_position'] =='slow':
    x_incriment = 1
elif alien_0['x_position'] == 'medium':
    x_incriment = 2
else:
# this is a fast alien
    x_incriment = 3
#The new postions is the old position plus the incriment
alien_0['x_position'] = alien_0['x_position'] + x_incriment

print(f"New x-position: {str(alien_0['x_position'])}")
