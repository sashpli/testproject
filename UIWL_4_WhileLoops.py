# WHILE Loop runs as long as a certain condition is TRUE
# counting numberes
current_number = 1              # value ist gesetzt auf  1
while current_number <= 5:      # RUN so lange die Bedingung WAHR IST
    print(current_number)       # Print current_number
    current_number += 1         # Zu current_number wird 1 addiert - Loop läuft von vorne -> current_number ist 2
    # current_number = current_number + 1

# Letting the User chose when to quit
# parrot.py RUN bis User "quit" schreibt
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nWrite 'quit' to exit the program."
message = ""                    # PY muss Variable kennen bevor sie geprüft wird. Es ist kein "quit" da "" also WAHR - Loop läuft
while message != "quit":        # RUN solange message NICHT QUIT ist WAHR ist!
    message = input(prompt)     # Usereingabe wird in message gespeichert
    print(message)              # Gibt message Usereingabe wieder aus.