#!/usr/bin/python3
x = 0; y = 0
directions = ["вверх","вниз","влево","вправо"]
move = input("Введите, куда вы хотите направиться(вверх,вниз,влево,вправо)\n");move = move.lower()
if not move in directions:
    print("Ошибка: Неизвестное направление")
else:
    steps = input("Введите, на сколько шагов вы хотите пойти в этом направлении\n")
    if(steps.isdigit()):
        steps = int(steps)
        if(move=="вправо"):
            x += steps
        elif(move=="влево"):
            x -= steps
        elif (move == "вверх"):
            y += steps
        elif (move == "вниз"):
            y -= steps
        print(f"Теперь вы находитесь в позиции {x, y}")
    else:
        print("Ошибка: необходимо вводить только числа и только положительные целые!")
