#!/usr/bin/python3
import os
print(f"Имя вашей операционной системы: {os.name}")
print(f"Имя вашего пользователя: {os.getlogin()}")
print("Список файлов и директорий в текущей папке:")
print(os.listdir(path="."))
