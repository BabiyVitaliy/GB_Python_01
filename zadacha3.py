# 3. Одинаковая четность Даны два целых числа: A, B. Проверить истинность высказывания: "Числа A и B имеют одинаковую четность".

a = int(input("Введите первое число "))
b = int(input("Введите второе числе "))

print("Чётность", a%2==b%2)