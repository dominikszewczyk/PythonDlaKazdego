a, b, c = map(int, input("Podaj zakres od, do oraz skok (oddzielając spacjami): ").split())

numbers = range(a, b, c)

print(list(numbers))