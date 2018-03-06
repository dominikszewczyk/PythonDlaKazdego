import random

liczba = random.randint(1, 5)
wrozba = ["Odważnie podążaj naprzód – nie musisz się niczego bać, ponieważ w tym roku jesteś całkowicie bezpieczny.",
          "Pracuj ciężko, ale mądrze – nie bierz wszystkiego na swoje barki. Pozwól, by inni ci pomogli, a odniesiesz sukces.",
          "Kieruj się rozsądkiem, a nie emocjami. Dzięki temu uchronisz się przed większością problemów.",
          "Nie unikaj swoich obowiązków i nie uciekaj przed życiowymi wyzwaniami. Choć czasami jest naprawdę trudno, warto podjąć wysiłek.",
          "Co dajesz, to otrzymujesz – pamiętaj o tej uniwersalnej i ponadczasowej zasadzie."]

print("Wylosowałeś wróżbę numer: {}, która brzmi:\n{}".format(liczba, wrozba[liczba-1]))
