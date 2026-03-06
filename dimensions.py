# Learning Tuples
# Lists work well for storing sets of items that can change throughout the
# life of a program. The ability to modify lists is particularly important when
# you’re working with a list of users on a website or a list of characters in a
# game. However, sometimes you’ll want to create a list of items that cannot
# change. Tuples allow you to do just that. Python refers to values that cannot
# change as immutable, and an immutable list is called a tuple.\
# A tuple looks just like a list except you use parentheses instead of square
# brackets. Once you define a tuple, you can access individual elements by
# using each item’s index, just as you would for a list.
from looping_lists import pizza

dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 1000)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

foods = ('ham and eggs' , 'soup' , 'spaghetti' , 'toast' , 'beans')
for food in foods:
    print(food)
print("\n")
# foods[0] = 'pizza'
# print(foods)
foods = ('pizza' , 'soup' , 'spaghetti' , 'toast' , 'beans')
for food in foods:
    print(food)