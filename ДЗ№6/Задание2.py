#!/usr/bin/python3
f = open('Input.txt','r')
f1 = open('Output.txt','w')
try:
    C,H,O = map(int,f.readline().split())
    c = 0
    while C>=2 and H>=6 and O>=1:
        c+=1
        C-=2
        H-=6
        O-=1
    f1.write(str(c))
except ValueError:
    f1.write("Ошибка: похоже, во входном файле что-то не так: или вы указали не все параметры или ввели не число")
