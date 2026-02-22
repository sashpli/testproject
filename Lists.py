persons = [ 'albert einstein' , 'alfred nobel' , 'mr. beast' , 'george washington' ]
#not_invited = persons.pop(2)
#print(f"I would like to invite:\n1. {persons[0].title()} \n2. {persons[2].title()} \nto my dinner")
#print(f"{not_invited.title()} is not invited")
invite = "Dear "
invite_2 = " herewith you are invited to my dinner"
print(invite + persons[0].title() + invite_2)
print(invite + persons[2].title() + invite_2)
print(invite + persons[1].title() + invite_2)
