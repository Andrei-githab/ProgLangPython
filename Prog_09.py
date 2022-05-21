"""
Лабораторная работа 9
Берем 8ю. добавляем в нее следующий функционал
По нажатию на клавиатуре (WASD) ваша окружность
перемещается на 1 в нужное направление, ответ
обновляется, рисунок обновляется.
Добавить блок обработку исключений на ввод
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from mpl_toolkits.axisartist import AxesZero
import keyboard
fig = plt.figure()
ax = fig.add_subplot(axes_class=AxesZero)
file = open('input_08.txt')
s = []
plt.ion()

for direction in ["xzero", "yzero"]:
    ax.axis[direction].set_axisline_style("-|>")
    ax.axis[direction].set_visible(True)

for direction in ["left", "right", "bottom", "top"]:
    ax.axis[direction].set_visible(False)

for row in file:
    digit = row.split()
    s.append(digit)
print(s)


try:
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
    circle_r = float(s[3][0])
    circle_x = float(s[3][1])
    circle_y = float(s[3][2])
    check_circle = False

    def drow_circ():
        global check_circle
        global Circ
        global out
        if (point_x - circle_x) ** 2 / circle_r ** 2 + (point_y - circle_y) ** 2 / circle_r ** 2 < 1:

            Circ=plt.Circle((circle_x, circle_y), circle_r, color='#BF3030', alpha=0.5)
            out=ax.add_patch(Circ)

            check_circle=False
            print("Точка принадлежит окружности")
        elif (point_x - circle_x) ** 2 / circle_r ** 2 + (point_y - circle_y) ** 2 / circle_r ** 2 == 1:
            Circ = plt.Circle((circle_x, circle_y), circle_r, edgecolor='r', facecolor='w')
            out=ax.add_patch(Circ)
            print("Точка лежит на окружности")
            check_circle=False
        else:

            Circ = plt.Circle((circle_x, circle_y), circle_r, edgecolor='b', facecolor='w')
            out=ax.add_patch(Circ)
            check_circle = True
            print("Точка не принадлежит окружности")

    if (line_x1 - point_x) * (line_y2 - point_y) - (line_x2 - point_x) * (line_y1 - point_y) == 0:
        # plt.plot([float(s[1][0]), float(s[1][2])], [float(s[1][1]), float(s[1][3])], c='red')  # прямая
        if line_x1 == line_x2 and line_y1 != line_y2:
            plt.axvline(x=line_x1, color='r')  # прорисовка прямой линии параллельно x , красного цвета ('r')
        elif line_x1 != line_x2 and line_y1 == line_y2:
            plt.axhline(y=line_x1, color='r')  # прорисовка прямой линии параллельно y , красного цвета ('r')
        print("Лежит на прямой")
    else:
        # plt.plot([float(s[1][0]), float(s[1][2])], [float(s[1][1]), float(s[1][3])], c='blue')  # прямая
        if line_x1 == line_x2 and line_y1 != line_y2:
            plt.axvline(x=line_x1, color='b')  # прорисовка прямой линии параллельно x , синего цвета ('b')
        elif line_x1 != line_x2 and line_y1 == line_y2:
            plt.axhline(y=line_x1, color='b ')  # прорисовка прямой линии параллельно y , синего цвета ('b')
        check_line = True
        print("Не лежит на прямой")

    if point_x < rectangle_x1 or point_x > rectangle_x2 or point_y < rectangle_y1 or point_y > rectangle_y2:
        ax.add_patch(patches.Rectangle((rectangle_x1, rectangle_y1), width, height, edgecolor='b',
                                       facecolor='w'))  # edgecolor='b'-цвет грани , facecolor='w'-цвет заливки
        print('не попадает в прямоугольник')
        check_rectangle = True
    elif point_x == rectangle_x1 or point_x == rectangle_x2 or point_y == rectangle_y1 or point_y == rectangle_y2:
        ax.add_patch(patches.Rectangle((rectangle_x1, rectangle_y1), width, height, edgecolor='r', facecolor='w'))

        print('попадает на границу прямоугольника ')
    else:
        ax.add_patch(patches.Rectangle((rectangle_x1, rectangle_y1), width, height, color='r',
                                       alpha=0.5))  # color='r' -цвет заливки, alpha=0.5 - прозрачность

        # plt.plot([rectangle_x1, rectangle_y1], [rectangle_x4, rectangle_y4], c='red')
        # plt.plot([rectangle_x4, rectangle_y4], [rectangle_x2, rectangle_y2], c='red')
        # plt.plot([rectangle_x2, rectangle_y2], [rectangle_x3, rectangle_y3], c='red')
        # plt.plot([rectangle_x3, rectangle_y3], [rectangle_x1, rectangle_y1], c='red')
        # plt.fill_between(x=[rectangle_x1, rectangle_x4], y1=rectangle_y1, y2=rectangle_y2, color='#BF3030', alpha=0.5)
        print('попадает внутрь прямоугольника')
    plt.scatter(float(s[0][0]), float(s[0][1]), c='black')  # ТОЧКА
    drow_circ()
    while True:

        # --------------------------Проверка на вхождение окружность----------------------
        try:
            if keyboard.is_pressed('w'):

                out.remove() #удаляем Circ = plt.Circle((circle_x, circle_y), circle_r, edgecolor='r', facecolor='w')
                                #out=ax.add_patch(Circ)
                circle_y+=1
                drow_circ() #рисуем новый круг с новой координатой цвыфвцццццццццццввффвыфф
                print('Смещение вверх')

            elif keyboard.is_pressed('s'):
                out.remove()
                circle_y-=1
                drow_circ()
                print('Смещение вниз')
            elif keyboard.is_pressed('a'):
                out.remove()
                circle_x-=1
                drow_circ()
                print('Смещение влево')
            elif keyboard.is_pressed('d'):
                out.remove()
                circle_x+=1
                drow_circ()
                print('Спещение вправо')
        except:
            break




        if check_rectangle == True and check_line == True and check_circle == True:  # проверяем, если точка не принадлежит ни одной из фигур
            ax.patch.set_facecolor('red')   # то красим фон в красный
            ax.patch.set_alpha(0.6)  # c прозрачьностью 0.6
        else: ax.patch.set_facecolor('w')
        plt.show() #Показать все открытые фигуры.   Подробнее:  https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.show.html

        fig.canvas.draw()
        fig.canvas.flush_events()
    print(s)
except ValueError:
    print('Неверный тип данных')

except IndexError:
    print("Отуствует одно из значений")
    print('''    Точка: x y
    Линия: x1 y2 x2 y2
    Прямоугольник: x1 y1 x2 y2
    Окружность: r(радиус) x  y''')
