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