#!/usr/bin/python3
def passw(str):
    c = 0
    for i in str:
        if i.isdigit():
            c += 1
    if len(str) >= 6 and c >= 1 and not str.isdigit() and str.lower().count("password") == 0:
        return True
    else:
        return False

n = input("Введите пароль, чтобы проверить надёжен ли он: ")
if passw(n):
    print("Ваш пароль удовлетворяет условиям")
else:
    print("Ваш пароль ненадёжен, измените его с учетом условий:")
    print("Должен быть не менее 6 символов\n"
          "Должен содержать хотя бы одну цифру\n"
          "Не должен состоять только из цифр\n"
          "Не должен содержать слово “password” в любом регистре")
