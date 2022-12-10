#!/usr/bin/python3
def summa(s):
    try:
        a = map(int, s.split())
        print(f"Сумма введенных чисел = {sum(a)}")
    except ValueError:
        print("Ошибка: похоже, вы ввели не только числа")
summa(input("Вводите числа, которые хотите просуммировать: "))

