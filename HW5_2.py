"""Дана строка (возможно, пустая), состоящая
из букв A-Z:
AAAABBBCCXYZDDDDEEEFFFAAAAAABBBB
BBBBBBBBBBBBBBBBBBBBBBBB
Нужно написать функцию RLE,
которая на выходе даст строку вида:
A4B3C2XYZD4E3F3A6B28
И сгенерирует ошибку, если на вход пришла
невалидная строка.
Пояснения: Если символ встречается 1 раз,
он остается без изменений; Если символ
повторяется более 1 раза, к нему
добавляется количество повторений"""

a = input("Введите строку ")

aunical = set(a)
diction = {}

check = True
for index in a:
    if ord(index) < 64 or ord(index) > 91:
        print("не подходяющая строка")
        check = False
        break

if check:
    for ch in aunical:
        count = 0
        for ch2 in a:
            if ch == ch2:
                count += 1
        diction[ch] = count
    for el in diction:
        print(el, end='')
        print(diction[el], end='')
