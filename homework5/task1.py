""" Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8  """

b= int(input("Введите числа b"))
n= int(input("Введите числа n "))
def expt(b, n):
    if n==0:
        return 1
    return b*expt(b, n-1)
    
print(expt(b,n))

