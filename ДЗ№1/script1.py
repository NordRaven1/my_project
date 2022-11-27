#!/usr/bin/python3
# Ближайшие простые числа
A = int(input())
def simple(x):
    c = 0; d = 2
    while d*d <= x:
        if x%d == 0:
            c = c+1
            break
        d = d+1
    if c == 0:
        return 1
    else:
        return 0
pred = posle = 0
n = 1; m = A
while n <= A:
    if simple(n) == 1 and n > pred:
        pred = n
    n += 1
while posle == 0:
    if simple(m) == 1 and m > posle:
        posle = m
    m += 1
print(pred,posle)