import sys, pickle


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


def get_result(file_name):
    file = open_file(file_name, "rb")
    names = pickle.load(file)
    scores = pickle.load(file)
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


file = open_file("score72.dat", "rb")
names = pickle.load(file)
scores = pickle.load(file)
file.close()
print(names)
print(scores)

name = "ja"
score = 3

names.append(name)
scores.append(score)

print(names)
print(scores)
