alien_color = 'green'
if alien_color == 'green':
    print('You just earned 5 points')

alien_color = 'green'
if alien_color == 'green':
    print('You just earned 5 points')
else:
    print('You just earned 10 points')

alien_color = 'red'
if alien_color != 'green': #Hier habe ich is not green und einfach die Punkte umngetauscht
    print('You just earned 10 points')
else:
    print('You just earned 5 points')

alien_color = 'yellow'
if alien_color == 'green':
    print('You just earned 5 points')
else:
    print('You just earned 10 points')
print("\n")
alien_color = 'green'
if alien_color == 'green':
    print('You just earned 5 points')
elif alien_color == 'yellow':
    print('You just earned 10 points')
elif alien_color == 'red':
    print('You just earned 15 points')

print("\n")

years = 5
if years <= 2:
    print('Your are still a baby')
elif years <= 4:
    print('You are a toddler')
elif years <= 13:
    print('You are a kid')
elif years <= 20:
    print('You are a teenager')
elif years <= 65:
    print('You are an adult')
else:
    print('You are an elder')

favorite_fruits = ['banana' , 'peach' , 'watermelon' , 'apple']
if 'banana' in favorite_fruits:
    print('You really like bananas')
if 'peach' in favorite_fruits:
    print('You really like peaches')
if 'watermelon' in favorite_fruits:
    print('You really like watermelons')


aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'speed': 'slow', 'points': 10}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
for alien in aliens[:5]:
    print(alien)
print("...")
print(f"Total numbers of aliens {len(aliens)}")






cars = []
for car_number in range(20):
    new_car = {'color': 'black', 'speed': 'slow', 'price': 50000}
    cars.append(new_car)
for car in cars[0:3]:
    if car['color'] == 'black':
        car['color'] = 'red'
        car['speed'] = 'fast'
        car['price'] = 80000
for car in cars[3:6]:
    if car['color'] == 'black':
        car['color'] = 'blue'
        car['speed'] = 'extreme'
        car['price'] = 150000
for car in cars[:10]:
    print(car)
print(f"Total numbers of cars {len(cars)}")


