from functools import reduce
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits),
# которая среди списка орбит планет найдет ту,
# по которой вращается самая далекая планета.
""" orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3), (11, 11)]


def find_farthest_orbit(orbits):
    result = orbits[0]
    for i in orbits:
        if result < i:
            result = i
            a, b = i

    return result, (a*b)


print(find_farthest_orbit(orbits))
 """
for i in range(10):
    for j in range(10):
        print( i*j )
    


""" def same_by(characteristic, objects):
    return len(set(map(characteristic, objects))) == 1

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different') """