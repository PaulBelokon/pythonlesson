import random
""" Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5 """
numberinlist = int(input("Введите ваш диапазон : "))
xnumbersearch = int(input("Введите ваше число для поиска: "))
list = [i for i in range(numberinlist)]

print(list)

result1 = xnumbersearch
for i in list:
    result = abs(i - xnumbersearch)
    if result == 1:
        count = i
        break
print(count)
