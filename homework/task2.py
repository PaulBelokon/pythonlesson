
while True:

    total = int(input("Общее количество журавликов: "))
    if total % 2 == 0:

        break

    print("Введены неверные данные")


numberKate = round(total // 1.5)
numberSergey = numberKate // 4
numberPetr = numberKate // 4

print(
    f" Ребенок Катя {numberKate},Ребенок Сережа {numberSergey},Ребенок Петя {numberPetr}")
