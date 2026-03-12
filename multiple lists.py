hello_admin = ['john' , 'max' , 'ted' , 'admin' , 'bob']
for name in hello_admin:
    if name == 'admin':
        print("Hello admin would you like to see a status report?")
    else:
        print(f"Hello {name.title()}, thank you for logging in again!")

print("\n")

hello_admin = []
if hello_admin:
    for name in hello_admin:
        if name == 'admin':
            print("Hello admin would you like to see a status report?")
        else:
            print(f"Hello {name.title()}, thank you for logging in again!")
else:
    print("We need more users")

print("\n")

current_users = ['john' , 'max' , 'ted' , 'admin' , 'bob']
new_users = ['seb' , 'alonso' , 'Max' , 'bob' , 'theodore']
for user in new_users:
    if user.lower() in current_users:
        print(f"{user.title()} has been used")
    else:
        print(f"{user.title()} is available")