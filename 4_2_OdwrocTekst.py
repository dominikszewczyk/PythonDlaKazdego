message = input("Podaj komunikat: ")

new_message = ""
for i in range(len(message)-1, -1, -1):
    new_message += message[i]

print(new_message)

new_message = message[::-1]
print(new_message)
