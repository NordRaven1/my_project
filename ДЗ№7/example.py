#!/usr/bin/python3
def hello(name):
    print(f"Hello {name}!")


def whole_and_remainder():
    try:
        x, y = map(int, input("Введите два числа: ").split())
        print(f"Целая часть = {x // y}")
        print(f"Остаток от деления = {x % y}")
    except ValueError:
        print("Кажется вы что-то напутали при вводе")
