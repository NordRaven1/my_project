#!/usr/bin/python3
# Было

# names = ["red","orange","green","yellow","black","brown","blue","pink","gray","violet","white","cyan"]
# codes = [(255,0,0),(255,165,0),(0,255,0),(255,255,0),(0,0,0),(150,75,0),(0,0,254),(255,105,180),(128,128,128),(134,1,175),(255,255,255),(64,224,208)]
# c = 0
# colors = dict.fromkeys(names)
# for i in colors:
#     colors[i] = codes[c]
#     c+=1
# print("Словарь цветов и их rgb кодировок:")
# for i in colors.items():
#     print(i)

# Стало

names = ["red", "orange", "green", "yellow",
         "black", "brown", "blue", "pink",
         "gray", "violet", "white", "cyan"]
codes = [(255, 0, 0), (255, 165, 0), (0, 255, 0), (255, 255, 0),
         (0, 0, 0), (150, 75, 0), (0, 0, 254), (255, 105, 180),
         (128, 128, 128), (134, 1, 175), (255, 255, 255), (64, 224, 208)]
c = 0
colors = dict.fromkeys(names)
for i in colors:
    colors[i] = codes[c]
    c += 1
print("Словарь цветов и их rgb кодировок:")
for i in colors.items():
    print(i)
