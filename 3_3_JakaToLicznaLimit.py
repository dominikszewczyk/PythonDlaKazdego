import random

name = input("Cześć! Zagrajmy w zgadnij liczbę :-)\nNapisz mi tylko jak masz na imie: ")

number = random.randint(1, 100)
print("Wylosowano liczbę z przedziału 1 do 100.\n{} jesteś gotowy??? Zaczynajmy!".format(name))

count_number = int(input("Ilu prób potrzebujesz na odgadniecie? "))
count = 1
while count <= count_number:
    number_type = int(input("Próba numer {}: ".format(count)))

    if(number_type == number):
        print("Udało Ci się zgadnąć za {} próbą. Gratulacje!".format(count))
        break
    elif(number_type < number):
        print("Tochę za mała ta liczba :-(. Spróbuj podać większą :-)")
    elif(number_type > number):
        print("Ojj... {} za duża ta liczba. Spróbuj podać mniejszą :-)".format(name))

    count += 1
