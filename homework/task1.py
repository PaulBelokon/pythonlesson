
while True:

    number = int(input("Введите трехзначное число: "))
    if number > 100 and number < 1000:

        break

    print("Введены неверные данные")
i = 0
sum = 0
while i < 4:
    sum = sum + number % 10
    number //= 10
    i = i + 1
else:
    print(f"Сумма цифр в числе равна {sum}")
