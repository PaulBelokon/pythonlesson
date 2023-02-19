# from array import *


# def input_array():
#     sixnumber = array('Q')
#     i = 0

#     while i < 6:
#         sixnumber[i] = int(input("Число массива "))
#         i = i+1
#         break

#         sum32 = sixnumber[3]+sixnumber[4]+sixnumber[5]
#         sum3 = sixnumber[0]+sixnumber[1]+sixnumber[2]
#     if sum3 == sum32:
#         print("Счастливое число)")
#     else:
#         print("Не удачно(")

# input_array()


while True:

    number = int(input("Ваше число: "))
    if 99999 < number and number < 1000000:

        break

    print("Введены неверные данные")

firsthalfnumber = (number // 1000)

i = 0
sum1 = 0
while i < 4:
    sum1 = sum1 + firsthalfnumber % 10
    firsthalfnumber //= 10
    i = i + 1
else:
    print(f"Сумма цифр в числе равна {sum1}")


secondhalfnumber = number % 1000


i = 0
sum2 = 0
while i < 4:
    sum2 = sum2 + secondhalfnumber % 10
    secondhalfnumber //= 10
    i = i + 1
else:
    print(f"Сумма цифр в числе равна {sum2}")

if sum1 == sum2:
    print("Ваш билет счастливый!")
else:
    print("Вам не повезло!")
