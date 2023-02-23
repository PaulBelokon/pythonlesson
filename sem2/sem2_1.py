number = int(input('Введите ваше число:  '))

count = 2
a = 0
b = 1
while b <= number:
    if b== number:
        print(count)
        break           
    a , b = b , a+b
    count += 1
else:
    print(-1)
