from traceback import print_tb

first_name = "Sasa"
last_name = "Pliso"
full_name = first_name + " " + last_name
print(full_name)

print(f"Hello {first_name} Would you like to learn pyhon today?")

print(first_name.title())
print(first_name.upper())
print(first_name.lower())

print('Albert Einstein once Seid "A person who never made a \nmistake never tried anything new"')

famous_person = "Albert Einstein"
print(f'{famous_person} once said, "A person who never made a mistake never tried anything new"')
message = ' once said, "TEST  person who never made a \nmistake never tried anything new"'
print(famous_person + message)

new_name = " Wilhelm "
print(new_name)
print(new_name.strip())
print(new_name.lstrip())
print(new_name.rstrip())
print(len(new_name.strip()))

print(0.2 + 0.1)

age = 23
message_2 = "Heppy " + str(age) + " Birthday!"
print(message_2)

print(4 + 4)
print(4 * 2)
print(16 //2)
print(10 - 2)

favorite_actor = "The guy who plays Batman"
print(favorite_actor)
print(age)

# comment
bicycles = ['trek', 'canondale' , 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[1].title())
print(bicycles[1].title().strip())
print(bicycles[1].strip().title())
print(bicycles[-1])

messege = "My first bicycle was a " + bicycles[-1].title() + "."
print(messege)
message_2 = "My " + bicycles[0].title() + " was stolen at a point"
print(message_2)
print(f"My first bicycle was a {bicycles[-1].title()} and it got stolen at a point")

names = [ "Bob" , "Alex" , "John"]
print(names[0])
print(names[1])
print(names[2])

messege_4 = "Hallo " + names[0].title() + " how are you?\nHow are you doing today " + names[1].title() + "?\nHow is " + names[2].title() + " doing?"
print(messege_4)
print(f"How is {names[0].title()} doing?\nAlso how is {names[1].title()} doing?")

cars = ['Alfa Rommeo' , 'Maserati' , 'Ferrari' , 'Honda']
print(f"I would like to drive a {cars[1]} someday")
cars_messege = "I would like to drive a " + cars[0] + " someday"
print(cars_messege)
cars_message_2 = ("I like " + cars[2] + "'s. But sometimes, its better to drive a reliable " + cars[3] + ".")
print(cars_message_2)
print(cars_messege + " " + cars_message_2 + "I dont know")
print(f"{cars_messege},\nbut I prefer japanese cars")
print(cars_messege + ", italian cars a great")

#adding a make afterword with append (appending)
motorcycles = ['honda' , 'yamaha' , 'suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

motorcycles_2 = [] #empty list, adding makes afterword
motorcycles_2.append('triumph')
motorcycles_2.append('BMW')
motorcycles_2.append('motor guzzi')
print(motorcycles_2)

#inserting elements into a list with .insert
motorcycles_2.insert(3, 'ducati')
print(motorcycles_2)

#removing item form list according to position or value with del
motorcycles_3 = ['Honda' , "BMW" , 'Motor Guzzi']
print(motorcycles_3)
del motorcycles_3[0]
print(motorcycles_3)

#pop() - Removes the last item on list - and lets you work with this item. The term pop comes from thinking of a list as a stack of items and popping one item off the top of the stack.

motorcycles_4 = ['A' , 'B' , 'C']
print(motorcycles_4)

popped_motorcycle = motorcycles_4.pop()
print(motorcycles_4)
print(popped_motorcycle)

last_owned = motorcycles_4.pop()
print("the last owned motorcycle is " + last_owned + "!")

cars_owned = ['Fiat' , 'Ford' , 'VW']
best_car = cars_owned.pop(0)
print(f"The best car I owned was a {best_car.upper()}.")

cars_owned_2 = ['Fiat' , 'Ford' , 'VW']
print(cars_owned_2)
cars_owned_2.remove('VW')
print(cars_owned_2)
to_expensive = "Ford"
cars_owned_2.remove(to_expensive)
print(cars_owned_2)
print("I sold the " + to_expensive + " because it was expensive")
