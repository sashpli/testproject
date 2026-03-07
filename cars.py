#if statements
#checking for equality

cars = ['audi' , 'bmw' , 'subaru' , 'toyota']
#ignoring cas when checking for equality
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'Audi'
car.lower() == 'audi'
print(car)

pizzas = ['salami' , 'tuna' , 'margerita']
for pizza in pizzas:
    if pizza == 'salami':
        print(pizza.upper())
    else:
        print(pizza.title())
#checking for inequality
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
#numerical comparisons
answer = 17
if answer != 42:
    print('That is not correct answer.')
else:
    print('That is the correct answer.')

print('\n')
#checking for multiple conditions with 'and' , 'or'
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

age_0 = 21
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)

#checking whether a value is in a list with 'in'

requested_toppings = ['mushrooms' , 'onions' , 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

print('\n')
participians = ['john' , 'ted' , 'Max']
# print('john' in participians)
# print('bob' in participians)
for participant in participians:
    if participant.lower() == 'max': #mit .lower die grosschreibung von Max auf max geändert
        print(f"Welcome {participant.title()}!")
    else:
        print("You are not a invited!")

#checking whether a value is not in a list with 'not'
banned_users = ['andrew' , 'carolina' , 'david']
user = 'bob'
if user.lower() not in banned_users:
    print(f"{user.title()} you can post a respons if you wish.")
else:
    print(f"{user.title()} you are banned!")

#boolean expressions. A boolean value is either True or False
car = 'subaru'
print(car == 'subaru')
print(car == 'audi')
print(car.lower() == 'subaru')

jobs = ['painter' , 'artist' , 'developer']
for job in jobs:
    if job != 'painter':
        print(f"{job.title()} is an interesting job")
    else:
        print(f"{job.title()} is boring job")

jobs = 'actor'
if jobs != 'astronaut':
    print(f"{jobs.title()} is a boring job")

jobs = 'actor'
if jobs == 'actor':
    print(f"{jobs.title()} is a interesting job")

salary = 2000
if salary == 2000:
    print(f"$ {salary} is not a bad salary.")

salary = 1999
if salary <= 2000:
    print(f"$ {salary} is not a bad salary.")

salary = 2001
if salary >= 2000:
    print(f"$ {salary} is not a bad salary.")

salary = 1212
if salary >= 2000:
    print(f"$ {salary} is not a bad salary.")
else:
    print(f"Your salary of $ {salary} is a bit on the side")

monthly_earnings = 4000
montly_losses = 3000
print(monthly_earnings >= 5000 and montly_losses <=3000)

monthly_earnings = 4000
montly_losses = 3000
print(monthly_earnings >= 5000 or montly_losses <=3000)

month_earnings = 2323
month_losses = 1232
if month_earnings <=5000 or month_losses >=3000:
    print(f"You are living way over your standards! You need to safe up more than $ {month_earnings - month_losses}")
else:
    print(f"Your total outcome is $ {month_earnings - month_losses}. And that is good budgeting")

list_companies = ['nvidia' , 'microsoft' , 'apple' , 'amazon']
print('nvidia' in list_companies)
print('microsoft' not in list_companies)

list_companies = ['nvidia' , 'microsoft' , 'apple' , 'amazon']
company = 'adobe'
if company not in list_companies:
    print(f"{company.title()} is banned from the list")

list_companies = ['nvidia' , 'microsoft' , 'apple' , 'amazon']
for company in list_companies:
    if company == 'nvidia' :
        print(f"{company.title()} that is a good company")

list_companies = ['nvidia' , 'microsoft' , 'apple']
for company in list_companies:
    if company != 'nvidia':
        print(f"{company.title()} is on the list")
    else:
        print(f"{company.title()} is not on the list")

colors = 'blue'
if colors != 'red':
    print(f"{colors.title()} is a good color")

colors = 'red'
if colors == 'red':
    print(f"{colors.title()} is a good color")








