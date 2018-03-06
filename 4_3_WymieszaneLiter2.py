import random

print("Witaj w grze 'Wymieszane litery'!")
print("Uporządkuj litery, aby odtworzyć prawidłowe słowo. Za odgadnięcie słowa dostajesz 10 punktów, za każdą podpowiedź tracisz 2 punkty.")
print("(Aby zakończyć grę, naciśnij ENTER bez podawania odpowiedzi)")

WORDS = ("dom", "komputer", "wiertarka", "lusterko", "python", "okulary")
word = random.choice(WORDS)
current = word

new_word = ""
while word:
    position = random.randrange(len(word))
    new_word += word[position]
    word = word[:position] + word[position+1:]

print("Zgadniej, jakie to słowo: {}".format(new_word))

points = 0
answer = input("\nTwoja odpowiedź: ")
while answer != current and answer != "":
    print("Niestety, to nie to słowo!")
    help = input("Czy chcesz uzyskac podpowiedź? (Tak/Nie)")
    if help.lower() == "tak":
        points += 1
        helper = current[:points]
        print("Podpowiedź: wyraz zaczyna się od liter: {}{}".format(helper, (len(current)-points)*" _"))
    answer = input("\nTwoja odpowiedź: ")

points = -points
if answer == current:
    points += 10
    print("Zgadza się! Zgadłeś - prawidłowe słowo to {}.".format(current))

print("Zdobyłeś {} punktów. Dziekujemy za udział w grze".format(points))
