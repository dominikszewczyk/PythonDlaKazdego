import random

choice = None
points = [0, 0, 0, 0]
names = ['Siła', 'Zdrowie', 'Mądrość', 'Zręczność']

while choice != "0":
    print("Do wykreowania postaci masz 30 punktów, które możesz przeznaczyć na cztery atrybuty: \n1. Siła: {} \n2. Zdrowie: {} \n3. Mądrość: {} \n4. Zręczność: {} \n"
          .format(points[0], points[1], points[2], points[3]))

    choice = input("Wybierz jedną z poniższych opcji: \n\t0. Zakończ program \n\t1. Podziel punkty \n\t2. Zmień podział punktów \nTwój wybór: ")

    if choice == "0":
        print("Koniec programu!")
    elif choice == "1":
        user_points = []
        user_points = list(map(int, input("Podaj wartości po spacjach: ").split()))
        if sum(user_points) <= 30:
            for i in range(4):
                points[i] = user_points[i]
        else:
            print("Rozdysponowales {} punktow, a masz tylkpo30 punktow. Sprobuj ponownie :-)".format(sum(user_points)))

    elif choice == "2":
        change_choice = int(input("Ktory atrybuj chcesz zmnienic? \n1. Siła: {} \n2. Zdrowie: {} \n3. Mądrość: {} \n4. Zręczność: {} \n ".format(points[0], points[1], points[2], points[3])))
        if change_choice in range(4):
            change_point = int(input("Podaj nowa liczb epunktow dla {}: ".format(names[change_choice])))
            if sum(points[:change_choice]) + sum(points[change_choice+1:]) + change_point <= 30:
                points[change_choice] = change_point
                print("Dodano {} punktow dla {}.".format(change_point, points[change_choice]))
            else:
                print("Rozdysponowales {} punktow, a masz tylko 30 punktow. Sprobuj ponownie :-)".format(sum(points[0:change_choice]) + sum(points[change_choice+1:3])))
        else:
            print("Dokonałeś niewłaściuwego wyboru! Spróbuj ponownie :)")
    else:
        print("Dokonałeś niewłaściuwego wyboru! Spróbuj ponownie :)")
