""" Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y(X, Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
 Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа. """
while True:

    sum = int(input("Ваша сумма чисел: "))
    multiplication = int(input("Ваше произведение чисел: "))

    if sum <= 2000 and multiplication <= 1000000:

        break

    print("Введены неверные данные")
for x in range(0, 1001):
    for y in range(0, 1001):
        if x + y == sum and x*y == multiplication:
            print(f"x = {x} y = {y}")