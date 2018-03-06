# Turniej wiedzy
# Gra sprawdzająca wiedzę ogólną, odczytująca dane ze zwykłego pliku tekstowego

import sys


def open_file(file_name, mode):
    """Otworz plik."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Nie mozna otworzyc pliku {}. Program zostanie zakonczony!\n{}".format(file_name, e))
        input("Aby zakończyć program, nacisnij klawisz Enter!")
        sys.exit()
    else:
        return the_file


def next_line(the_file):
    """Zwróc kolejny wiersz pliku po sformatowaniu go"""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line


def next_block(the_file):
    """Zwróć kolejny blok danych z pliku"""
    category = next_line(the_file)
    question = next_line(the_file)

    answers = []
    for i in range(4):
        answers.append(next_line(the_file))

    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    score_range = next_line(the_file)

    explanation = next_line(the_file)

    return category, question, answers, correct, score_range, explanation


def welcome(title):
    """Przywitaj gracza i pobierz jego nazwę"""
    print("\t\t Witaj w turnieju wiedzy!\n")
    print("\t\t {} \n".format(title))

    name = input("Powiedz nam jak się nazywasz... ")
    print("Dzień dobry {}".format(name))

    return name


def save_score(file_name, user_name, score):
    the_score_file = open_file(file_name, 'a')
    the_score_file.write("{} {}\n".format(user_name, score))
    the_score_file.close()
    print("Wyniki dla {} został dodane do listy!".format(user_name))


def main():
    trivia_file = open_file('kwiz71.txt', 'r')
    title = next_line(trivia_file)
    name = welcome(title)
    score = 0

    category, question, answers, correct, score_range, explanation = next_block(trivia_file)
    while category:
        print(category)
        print(question)
        for i in range(4):
            print("\t {}. {}".format(i+1, answers[i]), end=" ")

        answer = input("{} jaka jest Twoja odpowiedź?: ".format(name))

        if answer == correct:
            print("\nOdpowiedź prawidłowa!", end=" ")
            score += int(score_range)
        else:
            print("\nOdpowiedź niepoprawna!", end=" ")

        print(explanation)
        print("Wynik: {} \n\n".format(score))

        category, question, answers, correct, score_range, explanation = next_block(trivia_file)

    trivia_file.close()

    save_score('score73.txt', name, score)
    print("To było ostatnie pytanie!")
    print("Twój końcowy wynik wynosi: {}!".format(score))


main()
input("Aby zakończyć program, naciśnij klawisz Enter!")
