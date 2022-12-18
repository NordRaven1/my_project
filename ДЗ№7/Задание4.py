#!/usr/bin/python3
import numpy as np
a = np.random.randint(21,size=9).reshape((3, 3))
print(f"Изначальный массив:\n {a}")
print(f"Транспонированный массив:\n {a.transpose()}")
