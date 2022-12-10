#!/usr/bin/python3
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

n = input("Какой элемент ряда Фибоначчи вас интересует?: ")
if(n.isdigit()):
    n = int(n)
    if n == 0:
        print("Ошибка: такой элемент нельзя вычислить, нумерация начинается с 1")
    else:
        print(f"Данный элемент равен: {fib(n)} ")
else:
    print("Ошибка: вы ввели не числовое значение или отрицательное")
