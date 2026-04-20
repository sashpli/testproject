# WHILE Loop runs as long as a certain condition is TRUE
# counting numberes
current_number = 1              # value ist gesetzt auf  1
while current_number <= 5:      # RUN so lange die Bedingung WAHR IST
    print(current_number)       # Print current_number
    current_number += 1         # Zu current_number wird 1 addiert - Loop läuft von vorne -> current_number ist 2
    # current_number = current_number + 1

# Letting the User chose when to quit
# parrot.py RUN bis User "quit" schreibt
prompt = "\n1. Tell me something, and I will repeat it back to you: "
prompt += "\nWrite 'quit' to exit the program."
message = ""                    # PY muss Variable kennen bevor sie geprüft wird. Es ist kein "quit" da "" also WAHR - Loop läuft
while message != "quit":        # RUN solange message NICHT QUIT ist WAHR ist!
    message = input(prompt)     # Usereingabe wird in message gespeichert
    print(message)              # Gibt message Usereingabe wieder aus.

# Quit wird nicht gedruckt
prompt = "\n2. Tell me something, and I will repeat it back to you: "
prompt += "\nWrite 'quit' to exit the program."
message = ""
while message != "quit":
    message = input(prompt)
    if message != "quit":       # Erst print wenn message NICHT quit
        print(message)

# Using a Flag to end a Programm
# For a Programm that should RUN only as long as many conditions are TRUE
# FLAG acts a signal to the programm
# While statement needs only to check if the statement in the FLAG is TRUE

prompt = "\n3. Tell me something and I will repeat it back to you: "
prompt += "\nWrite 'quit' to exit the program. "
active = True                  # Program starts bc statement is TRUE
while active:                  # While active is TRUE
    message = input(prompt)    # Check Message after Userinput
    if message == "quit":      # If Userinput QUIT, active = False - While Loop stops
        active = False
    else:
        print(message)

# Using Break to exit a Loop
# To exit loop immediately without running any remaining code in the loop
# BREAK statement directs the flow of the program

prompt = "\n4. Please enter a name of a city you have visited."
prompt += "\nWrite 'quit' to exit the program. "

while True:
    city = input(prompt)

    if city == "quit":
        break
    else:
        print(f"I'd love to visit {city.title()}!")



