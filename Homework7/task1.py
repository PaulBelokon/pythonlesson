word = "аеуыоэяю"
inword = input().split()
list =[word.count(char) for word in inword
       for char in word if char.lower() in word]

if len(set(list)) == 1:
    print("Парам пам пам")
else:
    print("Пам парам")