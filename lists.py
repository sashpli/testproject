persons = ['albert einstein', 'alfred nobel', 'mr. beast', 'george washington']
#not_invited = persons.pop(2)
#print(f"I would like to invite:\n1. {persons[0].title()} \n2. {persons[2].title()} \nto my dinner")
#print(f"{not_invited.title()} is not invited")
#invite = "Dear "
#invite_2 = " herewith you are invited to my dinner"
#print(invite + persons[0].title() + invite_2)
#print(invite + persons[2].title() + invite_2)
#print(invite + persons[1].title() + invite_2)

print("The following persons are invited: " + persons[0].title() + ", " + persons[1].title() + ", " + persons[
    2].title() + ". " + persons[3].title() + " could not make it!")
del persons[3]
print(persons)
persons.append('donal trump')
print(persons)

print("All this persons are invited:" + persons[0].title() + ", " + persons[1].title() + ", " + persons[2].title() + ". " + persons[3].title())

persons.insert(0, 'danzel waschington')
persons.insert(2, 'barak obama')
persons.append('tom hanks')
print(persons)

first_person_1 = persons.pop(0)
print(first_person_1.title() + " sorry you are not longer invited")
first_person_2 = persons.pop(1)
print(first_person_2.title() + " you are not longer invited")
first_person_3 = persons.pop(2)
print(first_person_3.title() + " you are not longer invited")
first_person_4 = persons.pop(3)
print(first_person_4.title() + " you are not longer invited")
print(persons)
message = ("The following persons are still ivnited: ")
print(message + persons[0] + persons[1] + persons[2])
print(persons)
del persons[2]

print(persons)

#Sortin lists with sort() and sort(reverse=True)

cars = ['bmw' , 'audi' , 'toyota' , 'subaru']
#cars.sort()
#print(cars)
#cars.sort(reverse=True)
#print(cars)

print("Here is the original list: ")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the orginial list again: ")
print(cars)

cars = ['bmw' , 'audi' , 'toyota' , 'subaru']
cars.reverse()
print(cars)
cars.reverse()
print(cars)

len(cars)




