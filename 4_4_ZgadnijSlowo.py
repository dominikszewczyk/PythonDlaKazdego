import random

print("Witaj w grze 'Zgadnij słowo'! Zaczynamy...")
WORDS = ("dom", "komputer", "wiertarka", "lusterko", "python", "okulary")
word = random.choice(WORDS)
print(word)
length = len(word)

print("Masz 1 szans na zgadnięcie wyrazu, który ma {} słów. Oczywiście troszkę Ci podpowiem na początek. \n")

for i in range(5):
    help = input("Podaj literę, którą mam sprawdzić, czy występuje w moim słowie: ")
    if help in word:
        print("Literka {} - Tak".format(help))
    else:
        print("Literka {} - Nie".format(help))

answer = input("Nastła już ten momemnt, że musisz udzielić odpowiedzi. Słowo, którego szukasz to: ")

if answer.lower() == word.lower():
    print("Gratulację wygrałeś! Udało Ci się odgadąć słowo :-)")
else:
    print("Niestety Ci się nie udało. Słowo, które wylosowałem to: {}".format(word))
