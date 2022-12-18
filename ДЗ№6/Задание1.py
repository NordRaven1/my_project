#!/usr/bin/python3
def toBytes(mas):
    for i in range(0,len(mas)):
        mas[i] = ord(mas[i])

def toString(masb):
    for i in range(0,len(masb)):
        masb[i] = chr(masb[i])

str = list(input("Вводите любые символы: "))
toBytes(str)
print(f"Представление вашей строки  в виде байт кода: '{str}'")
toString(str)
print(f"Расшифровка вашей строки из байт кода обратно в строковое состояние: '{str}'")

