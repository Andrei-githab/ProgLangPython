import math

print("+++++++ Программа попадания точки в области +++++++\n")
print("-----> Прямая \n")

line_x1 = float(input("Введите X1: "))
line_y1 = float(input("Введите Y1: "))
line_x2 = float(input("Введите X2: "))
line_y2 = float(input("Введите Y2: "))

if line_x1 == line_x2:
    print("Прямая параллельна оси Oy и пересекает ее в точке с координатами [", line_x1, "; 0]")
elif line_y1 == line_y2:
    print("Прямая параллельна оси Oх и пересекает ее в точке с координатами [", line_y1, "; 0]")
else:
    line_k = (line_y1 - line_y2) / (line_x1 - line_x2)
    line_b = line_y1 - line_k * line_x1
    print("Уровнение прямой: Y = x *", round(line_k, 3), "+", round(line_b, 3))

print("\n-----> Прямоугольник")
pramul_x1 = float(input("Введите X1: "))
pramul_y1 = float(input("Введите Y1: "))
pramul_x2 = float(input("Введите X2: "))
pramul_y2 = float(input("Введите Y2: "))
pramul_x3 = float(input("Введите X3: "))
pramul_y3 = float(input("Введите Y3: "))
pramul_x4 = float(input("Введите X4: "))
pramul_y4 = float(input("Введите Y4: "))
print("Координаты прямоугольникa X1 >", pramul_x1, "Y1 >", pramul_y1, "X4 >", pramul_x4, "Y4 >", pramul_y4)

print("\n-----> Круг")
circle_x: float = float(input("Введите X: "))
circle_y = float(input("Введите Y: "))
circle_rad = float(input("Введите радиус: "))
print("Уровнение круга (X -", circle_x, ")^2 + (Y -", circle_y, ")^2 =", circle_rad)

print("\n-----> Точка")
x = float(input("Введите X: "))
y = float(input("Введите Y: "))
print("Координаты точки X >", x, "Y >", y)

print("\n##################################################\n")

if line_x1 == line_x2:
    if x < line_x1:
        print("Точка лежит слева")
    else:
        print("Точка лежит справа")
else:
    if y < line_k * x + line_b:
        print("Точка ниже прямой")
    else:
        print("Точка выше прямой")

if pramul_x1 <= x <= pramul_x2 and pramul_y1 <= y <= pramul_y2 and pramul_x3 <= x <= pramul_x4 and pramul_y3 <= y <= pramul_y4:
    print("Точка принадлежит прямоугольнику")
else:
    print("Точка НЕ! принадлежит прямоугольнику")


if (x - circle_x) ** 2 + (y - circle_y) ** 2 < circle_rad ** 2:
    print("Точка принадлежит кругу")
elif (x - circle_x) ** 2 + (y - circle_y) ** 2 > circle_rad ** 2:
    print("Точка НЕ! принадлежит кругу")
else:
    print("Точка на круге")
