#!/usr/bin/python3
#Выполнил это задание, используя функции. Хотя к занятию, к которому это задание привязано, они еще не изучены, думаю это не критично
Weight = 50 #Сделал константой, вроде нигде не было сказано, что значение надо вводить
Inventory = {}
actions = ["добавить","удалить","стоп"]

def putItem():
    global Weight
    n = input("\nВведите название предмета.Если добавляете одиннаковые предметы,\n"
              "необходимо в названии через пробел указать номер такого предмета. Иначе он 'исчезнет' :(\n"
              "Например, 'яблоко' и 'яблоко 2'\n")
    try:
        w = int(input("А теперь введите вес предмета: "))
    except ValueError:
        print("Вы ввели нечисловое значение, добавление предмета отменено")
        return 0
    if w > Weight:
        print("Это слишком тяжелый предмет, его нельзя положить в инвентарь. Придется нести в руках или выкинуть")
    else:
        Weight -= w
        Inventory[n] = w
        print(f"Предмет {n} добавлен в инвентарь")

def removeItem():
    global Weight
    trash = input("\nВведите название предмета, который вы хотите убрать из инвентаря: ")
    try:
        Weight += Inventory[trash]
        del Inventory[trash]
        print(f"Предмет {trash} убран из инвентаря")
    except KeyError:
        print(f"Вы что-то напутали - такого предмета({trash}) и не было в инвентаре")

def sortInventory(inv):
    sorted_inv = sorted(inv.values())
    InventoryLowToHigh = {}
    for i in sorted_inv:
        for k in inv.keys():
            if inv[k] == i:
                InventoryLowToHigh[k] = inv[k]
                break
    print("Ваш инвентарь:\nОт меньшего к большему(по весу):")
    for i in InventoryLowToHigh.items():
        print(i)
    InventoryHighToLow = dict(reversed(list(InventoryLowToHigh.items())))
    print("От большего к меньшему(по весу):")
    for i in InventoryHighToLow.items():
        print(i)

while True:
    action = input("\nВведите, что вы хотите сделать с инвентарем(добавить или удалить предмет) или 'стоп', если хотите закончить\n")
    action = action.lower()
    if not action in actions:
        print("Ошибка: Неизвестное взаимодействие с инвентарем")
        break
    elif (action == "стоп"):
        print("Вы закончили взамодействие с инвентарем, теперь вы увидите, что в нем сейчас находится")
        sortInventory(Inventory)
        break
    else:
        if action == 'добавить':
            putItem()
        else:
            removeItem()
