import random

licznik = 0
count_reszka = 0
count_orzel = 0

while licznik <= 100:
    # 0 - reszka, 1- orzelek
    los = random.randint(0, 1)
    if los == 0:
        count_reszka += 1
    elif los == 1:
        count_orzel += 1
    licznik += 1

print("Wylosowano {} reszkę i {} orzełka.".format(count_reszka, count_orzel))