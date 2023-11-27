from drawbot_skia.drawbot import rect, oval, saveImage

step = 150

#############
# задание 1 #
#############

# напишите цикл, рисующий по
# вертикали фигуры (квадраты
# или другие из ссылки выше)

y = 150
for i in range(5):
    rect(150, y, 100, 100)
    y = y + step

saveImage("output-01.pdf")

#############
# задание 2 #
#############

# напишите вложенный (двойной)
# цикл, заполняющий холст фигурами
# полностью, по вертикали и
# горизонтали

y = 150
x = 150
for i in range(5):
    for j in range(5):
        if (j % 2 == 0):
            rect(x, y, 100, 100)
        else:
            oval(x, y, 100, 100)
            
        x = x + 150
    
    x = step
    y = y + step

saveImage("output-02.pdf")