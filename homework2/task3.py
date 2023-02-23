""" Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N. """
numberdegree = int(input("Введите число: "))
result = 2
number = 2
i = 1
count =0
while result < numberdegree:
    result = number **i
    count+=1
    i+= 1
    if result < numberdegree:
        print(f" количество степеней {count}  число {result}")
    else:
        break