# Turniej wiedzy
# Gra sprawdzająca wiedzę ogólną, odczytująca dane ze zwykłego pliku tekstowego

import sys, pickle, os


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


def get_result(file_name):
    if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
        file = open_file(file_name, "rb")
        names = pickle.load(file)
        scores = pickle.load(file)
        file.close()
    else:
        file = open_file(file_name, "rb")
        names = []
        scores = []
        file.close()

    return scores, names


def save_result(name, score):
    scores, names = get_result("score72.dat")
    names.append(name)
    scores.append(score)
    file = open_file("score72.dat", "wb")
    pickle.dump(names, file, False)
    pickle.dump(scores, file, False)
    file.close()


def display_result():
    scores, names = get_result("score72.dat")
    for s, n in zip(scores, names):
        print("{}: {}".format(n, s))


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

        answer = input("Jaka jest Twoja odpowiedź?: ")

        if answer == correct:
            print("\nOdpowiedź prawidłowa!", end=" ")
            score += int(score_range)
        else:
            print("\nOdpowiedź niepoprawna!", end=" ")

        print(explanation)
        print("Wynik: {} \n\n".format(score))

        category, question, answers, correct, score_range, explanation = next_block(trivia_file)

    trivia_file.close()

    print("To było ostatnie pytanie!")
    save_result(name, score)
    display_result()
    print("Twój końcowy wynik wynosi: {}!".format(score))

main()
input("Aby zakończyć program, naciśnij klawisz Enter!")
