""" text = input().split()
print(text)
my_dict = {}

for i in text:
    if i in my_dict:
        print(f'{i}_{my_dict[i]}', end=' ')
    else:
        print(i, end=' ')
    my_dict[i] = my_dict.get(i, 0) + 1 """

"""     A = set(input('Введите строку: ').lower().split())
print(len(A)) """

