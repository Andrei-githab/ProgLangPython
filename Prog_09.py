"""
Лабораторная работа 9
Берем 8ю. добавляем в нее следующий функционал
По нажатию на клавиатуре (WASD) ваша окружность 
перемещается на 1 в нужное направление, ответ 
обновляется, рисунок обновляется.
Добавить блок обработку исключений на ввод
"""
import sys
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from mpl_toolkits.axisartist import AxesZero


def on_press(event):
    circle_r = float(s[3][0])
    circle_x = float(s[3][1])
    circle_y = float(s[3][2])
    check_circle = False
    print('press', event.key)
    sys.stdout.flush()
    if event.key == 'd':
        circle_x += 1
    elif event.key == 'a':
        circle_x -= 1
    elif event.key == 's':
        circle_y -= 1
    elif event.key == 'w':
        circle_y += 1
    if (point_x - circle_x) ** 2 / circle_r ** 2 + (point_y - circle_y) ** 2 / circle_r ** 2 < 1:
        ax.add_patch(plt.Circle((circle_x, circle_y), circle_r, color='#BF3030', alpha=0.5))
        print("Точка принадлежит окружности")
    elif (point_x - circle_x) ** 2 / circle_r ** 2 + (point_y - circle_y) ** 2 / circle_r ** 2 == 1:
        ax.add_patch(plt.Circle((circle_x, circle_y), circle_r, edgecolor='g', facecolor='w'))
        print("Точка лежит на окружности")
    else:
        ax.add_patch(plt.Circle((circle_x, circle_y), circle_r, edgecolor='r', facecolor='w'))
        return check_circle == True
        print("Точка не принадлежит окружности")
    fig.canvas.draw()


fig = plt.figure()
ax = fig.add_subplot(axes_class=AxesZero)
file = open('input_08.txt')
s = []

for direction in ["xzero", "yzero"]:
    ax.axis[direction].set_axisline_style("-|>")
    ax.axis[direction].set_visible(True)

for direction in ["left", "right", "bottom", "top"]:
    ax.axis[direction].set_visible(False)

'''
plt.xlabel('--Ось X-->', fontsize=20)  # подписываем ось  ('напдпись', размер шрифта) не очень красиво смотрится
plt.ylabel('--Ось Y-->', fontsize=20)  
'''

for row in file:
    digit = row.split()
    s.append(digit)
print(s)

point_x = float(s[0][0])
point_y = float(s[0][1])

rectangle_x1 = float(s[2][0])
rectangle_y1 = float(s[2][1])
rectangle_x2 = float(s[2][2])
rectangle_y2 = float(s[2][3])

rectangle_x3 = float(s[2][0])
rectangle_y3 = float(s[2][3])
rectangle_x4 = float(s[2][3])
rectangle_y4 = float(s[2][1])

width = rectangle_x2 - rectangle_x1
height = rectangle_y2 - rectangle_y1
check_rectangle = False

line_x1 = float(s[1][0])
line_y1 = float(s[1][1])
line_x2 = float(s[1][2])
line_y2 = float(s[1][3])
check_line = False

"""circle_r = float(s[3][0])
circle_x = float(s[3][1])
circle_y = float(s[3][2])"""

if (line_x1 - point_x) * (line_y2 - point_y) - (line_x2 - point_x) * (line_y1 - point_y) == 0:
    if line_x1 == line_x2 and line_y1 != line_y2:
        plt.axvline(x=line_x1, color='r')
    elif line_x1 != line_x2 and line_y1 == line_y2:
        plt.axhline(y=line_x1, color='r')
    print("Лежит на прямой")
else:
    if line_x1 == line_x2 and line_y1 != line_y2:
        plt.axvline(x=line_x1, color='b')
    elif line_x1 != line_x2 and line_y1 == line_y2:
        plt.axhline(y=line_x1, color='b')
    check_line = True
    print("Не лежит на прямой")

if point_x < rectangle_x1 or point_x > rectangle_x2 or point_y < rectangle_y1 or point_y > rectangle_y2:
    ax.add_patch(patches.Rectangle((rectangle_x1, rectangle_y1), width, height, edgecolor='r', facecolor='w'))
    print('не попадает в прямоугольник')
    check_rectangle = True
elif point_x == rectangle_x1 or point_x == rectangle_x2 or point_y == rectangle_y1 or point_y == rectangle_y2:
    ax.add_patch(patches.Rectangle((rectangle_x1, rectangle_y1), width, height, edgecolor='b', facecolor='w'))
    print('попадает на границу прямоугольника ')
else:
    ax.add_patch(patches.Rectangle((rectangle_x1, rectangle_y1), width, height, color='b', alpha=0.5))
    print('попадает внутрь прямоугольника')


plt.scatter(float(s[0][0]), float(s[0][1]), c='black')

fig.canvas.mpl_connect('key_press_event', on_press)

if check_rectangle == True and check_line == True:
    ax.patch.set_facecolor('b')
    ax.patch.set_alpha(0.6)

plt.show()
print(s)
