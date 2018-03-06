# Program symuluje telewizor
# Użytkownik ma możliwość wprowadznia numeru kanału oraz zwiększenia lub zmniejszenia głośności


class telewizor(object):
    """telewizor"""
    def __init__(self, channel=0, volume=0):
        self.channel = channel
        self.volume = volume
        print("Uruchomiłeś telewizor. \nAktualny kanał to: {}. \nAktualny poziom głośności to {}".format(channel, volume))

    def set_channel(self, channel):
        try:
            value = int(channel)
        except ValueError:
            print("Podana wartość '{}' nie jest liczbą. Spróbuj ponownie".format(value))
        else:
            if int(channel) <= 0 or int(channel) >= 25:
                print("Wykupiłeś tylko 25 kanałów. Inne są niedostępne w Twoim pakiecie.")
            else:
                self.channel = channel
                print("Ustawiłeś kanał {}.".format(channel))

    def set_volume(self, volume):
        try:
            value = int(volume)
        except ValueError:
            print("Podana wartość '{}' nie jest liczbą. Spróbuj ponownie".format(value))
        else:
            current_volume = self.volume + int(value)
            if int(value) > 0:
                result = "Zwiększyłeś"
            else:
                result = "Zmniejszyłeś"

            if current_volume < 0:
                self.volume = 0
                print("Zmniejszyłeś głośność do minimalnego poziomu. Aktualny poziom to {}.".format(self.volume))
            elif 0 <= current_volume <= 100:
                self.volume += value
                print("{} głośność o {}. Aktualny poziom głośności to {}".format(result, abs(value), self.volume))
            else:
                print("Zwiększyłeś głośnośc do maksymalnego poziomu. Aktualny poziom to {}.".format(self.volume))

    def show_settings(self):
        print("Kanał: {}".format(self.channel))
        print("Głośność: {}".format(self.volume))


def main():
    tv = telewizor()
    print()
    print\
    ("""Właśnie uruchomiłeś swój telewizor.
    Masz do dyspozycji 25 kanałów, które możesz oglądać kiedy tylko chcesz.
    Jeśli sobie zażyczysz możesz zmienić głośność telewizora. Pamiętaj jednak możesz operować w zakresie [0 - 100].:""")

    choice = None
    while choice != 0:

        print()
        print("""Na pilocie możesz wykonać poniższe operacje:
            0 - wyłącz
            1 - zmień kanał
            2 - zmien głośność
            3 - pokaż aktualne ustawienia""")

        choice = int(input("Wybierasz: "))
        print()

        if choice == 0:
            choice = 0

        elif choice == 1:
            channel = input("Na jaki kanał chcesz przełączyć? ")
            tv.set_channel(channel)

        elif choice == 2:
            volume = input("O ile chcesz zwiększyć lub mniejszyć głośność? ")
            tv.set_volume(volume)

        elif choice == 3:
            print("Aktualne ustawienia to: ")
            tv.show_settings()

        else:
            print("\nNiestety,", choice, "nie jest prawidłowym wyborem.")


main()
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
