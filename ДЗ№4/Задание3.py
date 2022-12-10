#!/usr/bin/python3
from random import randint
l1 = []; l2 = []
for i in range(0,10):
    n1 = randint(0, 20); n2 = randint(0, 20)
    l1.append(n1); l2.append(n2)
set1 = set(l1); set2 = set(l2)
print(f"Первое множество: {set1}")
print(f"Второе множество: {set2}")
s1 = set1.intersection(set2)
print(f"Элементы, принадлежащие обоим множествам: {s1}")
s2 = set1.difference(set2)
print(f"Элементы, принадлежащие только первому множестсву: {s2}")
s3 = set2.difference(set1)
print(f"Элементы, принадлежащие только второму множестсву: {s3}")
s4 = set1.symmetric_difference(set2)
print(f"Элементы, не принадлежащие обоим множествам одновременно: {s4}")
