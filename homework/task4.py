while True:

    numberX = int(input("Ваше число Х: "))
    numberY = int(input("Ваше число У: "))

    if numberX + numberY > 2:

        break

    print("Введены неверные данные")

while True:
    numberK = int(input("Ваше число К: "))
    if numberK%numberX==0 or numberK%numberY==0 and numberK<numberX*numberY:
        print("Ваше число К верно, можно разделить шоколадку")
        break
    print("Введены неверные данные числа К, шоколадка не разделится")
