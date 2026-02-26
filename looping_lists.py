magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    #print(f"Also {magician.title()} did a great job!")
    #print(f"I cant' wait to see your next trick, {magician.title()}.\n")
    print("I can't wait to see yur next trick, " + magician.title() + ".\n" )
print("Thank you, everyone. That was a great magic show!\n")

pizzas = ['margerita' , 'salami' , 'capriciosa']
for pizza in pizzas:
    print(pizza.title())
print(f"I really like all kind of pizzas, my favorite pizzas are: {pizzas[0].title()} and {pizzas[1].title()}. But a pizza {pizzas[2].title()} I'll also eat if there is no other choice.\nI really love pizza!\n")

animals = ['horse' , 'zebra' , 'giraffe']
for animal in animals:
    print(animal.title())
    print(f"A {animal.title()} would make a great pet\n")
print(f"All those animals have four legs in common, they would make a great pet\n")




