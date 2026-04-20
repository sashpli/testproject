# prompt = "Rechne folgende Zahlen zusammen 1+1= "
# active = True
# while active:
#     message = input(prompt)
#     if int(message) == 2:
#         active = False
#     else:
#         print("that's false")
#
# prompt = "Was is die Hauptstadt von der Schweiz? "
# while True:
#     message = input(prompt)
#     if message == "Bern":
#         print("Bern ist richtig")
#         break
#     else:
#         print("Das is nicht richtig!")

prompt = "Was is die Hauptstadt von der Schweiz? "
active = True
while active:
    message = input(prompt)
    if message == "zürich":
        active = False
        print("Zürich ist die größte Stadt, aber nicht die Hauptstadt, das Programm wird beendet")
    elif message == "Bern":
        active = False
        print(f"Genau {message.title()} ist die Hauptstadt von der Schweiz?")
    else:
        print(f"{message.title()} ist nicht die Hauptstadt!")
