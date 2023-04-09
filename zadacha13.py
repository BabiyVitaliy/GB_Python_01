"""Вы пользуетесь общественным транспортом? Вероятно, вы
расплачивались за проезд и получали билет с номером. Счастливым
билетом называют такой билет с шестизначным номером, где сумма
первых трех цифр равна сумме последних трех. Т.е. билет с номером
385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
программу, которая проверяет счастливость билета."""

a = int(input("Введите шестизначное число "))
while a < 100000 or a > 999999:
    a = int(input("Введите шестизначное число "))

print(a // 100000 + a // 10000 % 10 + a // 1000 % 10 == a // 100 % 10 + a // 10 % 10 + a % 10)