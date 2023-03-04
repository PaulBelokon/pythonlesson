import random
# Фибоначчи
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ...,
# где # a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи


def sum_fib(a):
    if a in [0, 1]:
        return 1
    return sum_fib(a-2)+sum_fib(a-1)


print(sum_fib(int(input())))


list = [random.randint(1,5) for i in range(int(input()))]
print(list)

