#!/usr/bin/python3
def passw(stroka):
    """"Проверяет, удовлетворяет ли переданный аргумент условиям

    Принимает:
        stroka - переменную типа 'строка'
    Возвращает:
        True или False
    """
    c = 0
    for i in stroka:
        if i.isdigit():
            c += 1
    if len(stroka) >= 6 and c >= 1 and not stroka.isdigit() and stroka.lower().count("password") == 0:
        return True
    else:
        return False


strochka = input("Введите пароль, чтобы проверить надёжен ли он: ")
if passw(strochka):
    print("Ваш пароль удовлетворяет условиям")
else:
    print("Ваш пароль ненадёжен, измените его с учетом условий:")
    print("Должен быть не менее 6 символов\n"
          "Должен содержать хотя бы одну цифру\n"
          "Не должен состоять только из цифр\n"
          "Не должен содержать слово “password” в любом регистре")
