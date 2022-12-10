#!/usr/bin/python3
mas = [5,23,17,59,32,354,12,0,6]
print(f"Изначальный массив чисел: {mas}")
N = len(mas)
for i in range(N-1):
    for j in range(N-i-1):
        if mas[j] > mas[j+1]:
            swap = mas[j]
            mas[j] = mas[j+1]
            mas[j+1] = swap
print(f"Отсортированный массив: {mas}")
