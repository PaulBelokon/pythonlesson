""" 7
# 3 1 3 4 2 4 12

# 6
# 4 15 43 1 15 1 """
""" count1 = int(input('Сколько элементов будет в первом массиве? —> '))
list1 = []
for _ in range(count1):
    list1.append(int(input('\tэлемент массива —> ')))
count2 = int(input('Сколько элементов dj втором массиве? —> '))
list2 = []
for _ in range(count2):
    list2.append(int(input('\tэлемент массива —> ')))

print([x for x in list1 if x not in (list2)]) """

""" list_1 = [1, 2, 3, 4, 5]
# list_2 = [1, 5, 1, 5, 1]
# list_3 = []
# count_1 = 0
# # n = int(input('Введите количество элементов первого массива: '))
# # for i in range(n):
# #     list_1.append(int(input('Введите элемент 1-ого массива: ')))
# for i in range(1, len(list_1)-1):
#     if (list_1[i] > list_1[i+1]) & (list_1[i] > list_1[i-1]):
#         count_1 += 1
# print(count_1)

list_1 = [1, 5, 1, 5, 1]

count_1 = 0
# n = int(input('Введите количество элементов первого массива: '))
# for i in range(n):
#     list_1.append(int(input('Введите элемент 1-ого массива: ')))
for i in range(1, len(list_1)-1):
    if list_1[i] == max(list_1[i-1:i+2]):
        count_1 += 1
print(count_1) """

""" 
li = [1, 2, 4, 2, 5, 1, 6, 4, 4]
sum = 0
for i in li:
    if li.count(i) > 1:
        if li.count(i) % 2 != 0:
            sum += (li.count(i) - 1) / 4
            li.pop(i)
        else:
            sum += li.count(i) / 4
        print(f'i = {li.count(i) / 4}, sum = {sum}') """


""" li = []
user_num = abs(int(input("Input a number: ")))

for i in range(2, user_num + 1):
    while user_num % i == 0:
        li.append(i)
        user_num //= i
    if user_num > 1 and user_num % i != 0:
        li.append(user_num)
        user_num //= user_num
li.append(1)
print(li) """