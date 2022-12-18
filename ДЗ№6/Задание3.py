#!/usr/bin/python3
f = open('Input.txt','r')
f1 = open('Output.txt','w')
key = list(f.readline()) # Предпологается, что сначала идет ключ, а потом текст в несколько строк
text = []
for line in f:
    for k in line:
        text.append(k)

def Shifr(mas,key):
    k = 0
    line = ''
    if len(mas)>0 and len(key)>0:
        for i in range(0,len(mas)):
            if k > len(key)-1:
                k = 0
            line += chr(ord(mas[i]) ^ ord(key[k]))
            k+=1
        f1.write(line)
    else:
        f1.write("Кажется вы не указли ключ или слово для (де)шифрования")

Shifr(text,key)
