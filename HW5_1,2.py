"""Напишите программу возведения числа в степень с помощью рекурсии"""

a = int(input("Введите число которое будем возводить в степень: "))
b = int(input("Введите значение стпени в которую будем возводить число: "))

def pow(a, b):
    if (b == 1):
        return (a)
    if (b != 1):
        return (a * pow(a,b-1))
print(a, "^", b, "=", pow(a,b))


"""Частотный массив строк A-Z"""


b = input("Введите строку ")

def func (a):
    textresult = ""
    aunical = set(a)
    diction = {}

    check = True
    for index in a:
        if ord(index) < 64 or ord(index) > 91:
            print("не подходит строка")
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
            if diction[el] == 1:
                textresult = textresult + str(el)
            else:
                textresult = textresult + str(el) + str(diction[el])
        return textresult
    return ""

print(func(b))