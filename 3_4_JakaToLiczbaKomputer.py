import random

name = input("Hej! :-) Jak masz na imie? ")
print("{} wylosowałeś już liczbę z przedziału 1 do 100? Możemy zaczynać grę?".format(name))

chance = int(input("Ile dasz mi szans na ogadnięcie twojej liczby? "))

count = 1
while count <= chance:
    number = random.randint(1, 100)
    answer = input("Mój typ to: {}. Udało mi się zgadnąć (w próbie {})? ".format(number, count))
    if answer.lower() == "tak":
        print("Udało mi się, ale się ciesze! :-)")
        break
    else:
        if count == chance:
            print("To już koniec gry. Nie udało mi sie odgadnąć.")
        else:
            print("Próbuje dalej... zostało mi jeszcze {} próby :-)\n".format(chance - count))
    count += 1
