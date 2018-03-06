# Opiekun zwierzaka
# Wirtualny pupil, którym należy się opiekować

class Critter(object):
    """Wirtualny pupil"""

    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "szczęśliwy"
        elif 5 <= unhappiness <= 10:
            m = "zadowolony"
        elif 11 <= unhappiness <= 15:
            m = "podenerwowany"
        else:
            m = "wściekły"
        return m

    def talk(self):
        print("Nazywam się {} i jestem {} teraz.\n".format(self.name, self.mood))
        print("Nazwa: {}, Głód: {}, Nuda: {}".format(self.name, self.hunger, self.boredom))
        self.__pass_time()

    def eat(self, food=4):
        print("Mniam, mniam... Dziękuję!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun=4):
        print("Hura! Dobra zabawa.")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def get_number(text):
    number_str = input(text)
    try:
        number_int = int(number_str)
        if number_int < 0:
            number_int = 0
    except ValueError:
        print("Podałeś '{}' i to nie jest liczba. Spróbuj ponownie! :-)".format(number_str))
        number_int = 0
        return number_int
    else:
        return number_int


def main():
    crit_name = input("Jak chcesz nazwać swojego zwierzaka? ")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        print("""
        Opiekun zwierzaka

        0 - zakończ
        1 - słuchaj swojego zwierzaka
        2 - nakarm swojego zwierzaka
        3 - pobaw się ze swoim zwierzakiem
        """)
        choice = input("Wybierasz: ")
        print()

        # wyjdź z pętli
        if choice == "0":
            print("Do widzenia.")

        # słuchaj swojego zwierzaka
        elif choice == "1":
            crit.talk()

        # nakarm swojego zwierzaka
        elif choice == "2":
            food = get_number("Ile jedzeniec chesz podać swojemu pupilowi? [1-10]: ")
            if food > 0:
                crit.eat(food)

        # pobaw się ze swoim zwierzakiem
        elif choice == "3":
            sport = get_number("Jak długo chcesz się bawić ze swoim pupilem? [1-10]: ")
            if sport > 0:
                crit.play(sport)

        # nieznany wybór
        else:
            print("Niestety {} nie jest prawidłowym wyborem".format(choice))


# Uruchomienie programu
main()
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
