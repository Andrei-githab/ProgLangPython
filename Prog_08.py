"""
Лабораторная работа 8
Написать программу попадания точки в области
(визуализированный вариант)
"""
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

s = []
plt.figure(figsize=(8, 8))
plt.gca().spines['left'].set_position('center')
plt.gca().spines['bottom'].set_position('center')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.grid(linestyle='--')


def line(x1_line, x2_line):
    plt.plot(x1_line, x2_line, color="k")


def rectangle(x_rectangle, l_rectangle, d_rectangle):
    currentAxis = plt.gca()
    currentAxis.add_patch(Rectangle(x_rectangle, l_rectangle, d_rectangle, facecolor="None", ec='k'))


def circle(x_circle, r_circle):
    circle1 = plt.Circle(x_circle, r_circle, color='None', ec='k')
    plt.gca().add_patch(circle1)


try:
    file = open("input_08.txt", "r")
    try:
        for row in file:
            digit = row.split()
            s.append(digit)
    except Exception as e:
        print(e)
    finally:
        file.close()
except Exception as ex:
    print(ex)


x_l, y_l, x_ll, y_ll = float(s[0][0]), float(s[0][1]), float(s[0][2]), float(s[0][3])
x_rec, y_rec, x_recc, y_recc = float(s[1][0]), float(s[1][1]), float(s[1][2]), float(s[1][3])
x_cer, y_cer, r_cer = float(s[2][0]), float(s[2][1]), float(s[2][2])
x_toh, y_toh = float(s[3][0]), float(s[3][1])


plt.text(7, 0, "X", fontsize=15)
plt.text(0, 7, "Y", fontsize=15)
plt.xlim(
    min(x_l, x_ll, x_rec, x_recc, x_cer - r_cer, x_toh, y_l, y_ll, y_rec, y_recc, y_cer - r_cer, y_toh, -x_l, -x_ll,
        -x_rec, -x_recc, -(x_cer - r_cer), -x_toh, -y_l, -y_ll, -y_rec, -y_recc, -(y_cer - r_cer), -y_toh,
        y_cer + r_cer, y_cer - r_cer, -y_cer - r_cer, -y_cer + r_cer) - 3,
    max(x_l, x_ll, x_rec, x_recc, x_cer - r_cer, x_toh, y_l, y_ll, y_rec, y_recc, y_cer - r_cer, y_toh, -x_l, -x_ll,
        -x_rec, -x_recc, -(x_cer - r_cer), -x_toh, -y_l, -y_ll, -y_rec, -y_recc, -(y_cer - r_cer), -y_toh,
        y_cer + r_cer, y_cer - r_cer, -y_cer - r_cer, -y_cer + r_cer) + 3)
plt.ylim(
    min(x_l, x_ll, x_rec, x_recc, x_cer - r_cer, x_toh, y_l, y_ll, y_rec, y_recc, y_cer - r_cer, y_toh, -x_l, -x_ll,
        -x_rec, -x_recc, -(x_cer - r_cer), -x_toh, -y_l, -y_ll, -y_rec, -y_recc, -(y_cer - r_cer), -y_toh,
        y_cer + r_cer, y_cer - r_cer, -y_cer - r_cer, -y_cer + r_cer) - 3,
    max(x_l, x_ll, x_rec, x_recc, x_cer - r_cer, x_toh, y_l, y_ll, y_rec, y_recc, y_cer - r_cer, y_toh, -x_l, -x_ll,
        -x_rec, -x_recc, -(x_cer - r_cer), -x_toh, -y_l, -y_ll, -y_rec, -y_recc, -(y_cer - r_cer), -y_toh,
        y_cer + r_cer, y_cer - r_cer, -y_cer - r_cer, -y_cer + r_cer) + 3)

plt.gca().add_patch(Rectangle((-10000, -10000), 20000, 20000, facecolor="cyan"))
l_tangle = max(x_rec, x_recc) - min(x_rec, x_recc)
d_tangle = max(y_rec, y_recc) - min(y_rec, y_recc)


def print_circle():
    ra = (x_toh - x_cer) * (x_toh - x_cer) + (y_toh - y_cer) * (y_toh - y_cer)

    if r_cer * r_cer < ra:
        plt.gca().add_patch(plt.Circle([x_cer, y_cer], r_cer, color='w', ))
    else:
        plt.gca().add_patch(Rectangle((-10000, y_cer + r_cer), 20000, 20000, facecolor="w"))
        plt.gca().add_patch(Rectangle((-10000, y_cer - r_cer), 20000, -20000, facecolor="w"))
        plt.gca().add_patch(Rectangle((x_cer + r_cer, y_cer + r_cer), 20000, -20000, facecolor="w"))
        plt.gca().add_patch(Rectangle((x_cer - r_cer, y_cer - r_cer), -20000, 20000, facecolor="w"))
        xp = np.array(
            [x_cer - r_cer, x_cer - r_cer * 0.98, x_cer - r_cer * 0.96, x_cer - r_cer * 0.94, x_cer - r_cer * 0.92,
             x_cer - r_cer * 0.9, x_cer - r_cer * 0.8, x_cer - r_cer * 0.7, x_cer - r_cer * 0.6, x_cer - r_cer * 0.5,
             x_cer - r_cer * 0.4, x_cer - r_cer * 0.3, x_cer - r_cer * 0.2, x_cer - r_cer * 0.1, x_cer,
             x_cer + r_cer * 0.1, x_cer + r_cer * 0.2, x_cer + r_cer * 0.3, x_cer + r_cer * 0.4, x_cer + r_cer * 0.5,
             x_cer + r_cer * 0.6, x_cer + r_cer * 0.7, x_cer + r_cer * 0.8, x_cer + r_cer * 0.9, x_cer + r_cer * 0.92,
             x_cer + r_cer * 0.94, x_cer + r_cer * 0.96, x_cer + r_cer * 0.98, x_cer + r_cer])
        yp = np.array([y_cer, y_cer + r_cer * 0.2, y_cer + r_cer * 0.28, y_cer + r_cer * 0.34, y_cer + r_cer * 0.4,
                       y_cer + r_cer * 0.43, y_cer + r_cer * 0.6, y_cer + r_cer * 0.71, y_cer + r_cer * 0.8,
                       y_cer + r_cer * 0.86, y_cer + r_cer * 0.91, y_cer + r_cer * 0.95, y_cer + r_cer * 0.98,
                       y_cer + r_cer * 0.99, y_cer + r_cer, y_cer + r_cer * 0.99, y_cer + r_cer * 0.98,
                       y_cer + r_cer * 0.95, y_cer + r_cer * 0.91, y_cer + r_cer * 0.86, y_cer + r_cer * 0.8,
                       y_cer + r_cer * 0.71, y_cer + r_cer * 0.6, y_cer + r_cer * 0.43, y_cer + r_cer * 0.4,
                       y_cer + r_cer * 0.34, y_cer + r_cer * 0.28, y_cer + r_cer * 0.2, y_cer])
        plt.fill_between(xp, yp, y2=y_cer + r_cer, color="w")
        yp = np.array(
            [y_cer, y_cer - r_cer * 0.2, y_cer - r_cer * 0.28, y_cer - r_cer * 0.34, y_cer - r_cer * 0.4,
             y_cer - r_cer * 0.43, y_cer - r_cer * 0.6, y_cer - r_cer * 0.71,
             y_cer - r_cer * 0.8, y_cer - r_cer * 0.86, y_cer - r_cer * 0.91, y_cer - r_cer * 0.95,
             y_cer - r_cer * 0.98, y_cer - r_cer * 0.99, y_cer - r_cer,
             y_cer - r_cer * 0.99, y_cer - r_cer * 0.98, y_cer - r_cer * 0.95, y_cer - r_cer * 0.91,
             y_cer - r_cer * 0.86, y_cer - r_cer * 0.8, y_cer - r_cer * 0.71,
             y_cer - r_cer * 0.6, y_cer - r_cer * 0.43, y_cer - r_cer * 0.4, y_cer - r_cer * 0.34, y_cer - r_cer * 0.28,
             y_cer - r_cer * 0.2, y_cer])

        plt.fill_between(xp, yp, y2=y_cer - r_cer, color="w")


def print_line():
    if x_l != x_ll:
        kx = (x_l - x_ll) / (y_l - y_ll)
        bx = -y_ll * (x_l - x_ll) / (y_l - y_ll) + x_ll
        ky = (y_l - y_ll) / (x_l - x_ll)
        by = -x_ll * (y_l - y_ll) / (x_l - x_ll) + y_ll

        if y_toh != x_toh * ky + by:
            if ((-1) - x_ll) / (x_l - x_ll) * (y_l - y_ll) + y_ll < (- x_ll) / (x_l - x_ll) * (y_l - y_ll) + y_ll:
                if bx < 0:
                    if y_toh > x_toh * ky + by:
                        plt.fill_betweenx([-10000, by], [-10000 * 1 / ky + by, 0], color="w")
                        plt.gca().add_patch(Rectangle((0, -10000), 10000, 10000, facecolor="w"))
                        plt.fill_between([bx, 0], [0, by], color="cyan")
                        plt.fill_between([bx, 10000], [0, 10000 * ky + by], color="w")
                    else:
                        plt.fill_between([-10000, bx], [-10000 * ky + by, 0], color="w")
                        plt.gca().add_patch(Rectangle((-10000, 10000), 10000, -10000, facecolor="w"))
                        plt.fill_between([bx, 0], [0, by], color="cyan")
                        plt.fill_betweenx([by, 10000], [0, 10000 * 1 / ky + by], color="w")

                else:
                    if y_toh > x_toh * ky + by:
                        plt.fill_betweenx([-10000, by], [-10000 * 1 / ky + by, 0], color="w")
                        plt.gca().add_patch(Rectangle((0, -10000), 10000, 10000, facecolor="w"))
                        plt.fill_between([bx, 0], [0, by], color="cyan")
                        plt.fill_between([bx, 10000], [0, 10000 * ky + by], color="w")
                    else:
                        plt.fill_between([-10000, bx], [-10000 * ky + by, 0], color="w")
                        plt.gca().add_patch(Rectangle((-10000, 10000), 10000, -10000, facecolor="w"))
                        plt.fill_between([bx, 0], [0, by], color="cyan")
                        plt.fill_betweenx([by, 10000], [0, 10000 * 1 / ky + by], color="w")

            elif ((-1) - x_ll) / (x_l - x_ll) * (y_l - y_ll) + y_ll > (-x_ll) / (x_l - x_ll) * (y_l - y_ll) + y_ll:
                if bx < 0:
                    if y_toh > x_toh * ky + by:
                        plt.fill_betweenx([-10000, by], [-10000 * 1 / ky + by, 0], color="w")
                        plt.gca().add_patch(Rectangle((-10000, -10000), 10000, 10000, facecolor="w"))
                        plt.fill_between([bx, 0], [0, by], color="cyan")
                        plt.fill_between([-10000, bx], [-10000 * ky + by, 0], color="w")
                    else:
                        plt.fill_between([0, 10000], [by, 10000 * ky + by], color="w")
                        plt.gca().add_patch(Rectangle((0, 0), 10000, 10000, facecolor="w"))
                        plt.fill_between([bx, 0], [0, by], color="cyan")
                        plt.fill_betweenx([by, 10000], [0, 10000 * 1 / ky + by], color="w")

                else:
                    if y_toh > x_toh * ky + by:
                        plt.fill_betweenx([-10000, by], [-10000 * 1 / ky + by, 0], color="w")
                        plt.gca().add_patch(Rectangle((-10000, -10000), 10000, 10000, facecolor="w"))
                        plt.fill_between([bx, 0], [0, by], color="cyan")
                        plt.fill_between([-10000, bx], [-10000 * ky + by, 0], color="w")
                    else:
                        plt.fill_between([-10000, bx], [-10000 * ky + by, 0], color="w")
                        plt.gca().add_patch(Rectangle((-10000, 10000), 10000, -10000, facecolor="w"))
                        plt.fill_between([bx, 0], [0, by], color="cyan")
                        plt.fill_betweenx([by, 10000], [0, 10000 * 1 / ky + by], color="w")
    else:
        if x_toh > x_l:
            plt.gca().add_patch(Rectangle((x_toh, 10000), 20000, -20000, facecolor="w"))
        else:
            plt.gca().add_patch(Rectangle((x_toh, 10000), -20000, -20000, facecolor="w"))


def print_recctangle():
    if (min(x_rec, x_recc) <= x_toh <= max(x_rec, x_recc)) and (min(y_rec, y_recc) <= y_toh <= max(y_rec, y_recc)):

        plt.gca().add_patch(Rectangle((-10000, max(y_rec, y_recc)), 20000, 20000, facecolor="w"))
        plt.gca().add_patch(Rectangle((-10000, max(y_rec, y_recc)), min(x_rec, x_recc) + 10000, -20000, facecolor="w"))
        plt.gca().add_patch(Rectangle((max(x_rec, x_recc), max(y_rec, y_recc)), 20000, -20000, facecolor="w"))
        plt.gca().add_patch(Rectangle((min(x_rec, x_recc), min(y_rec, y_recc)), 20000, -20000, facecolor="w"))
        print(1)
    else:
        plt.gca().add_patch(Rectangle(([min(x_rec, x_recc), min(y_rec, y_recc)]), l_tangle, d_tangle, facecolor="w"))
        print(2)


if x_l == x_ll:
    line([x_l, x_l], [-10000, 10000])
else:
    line([-10000, 10000],
         [(-10000 - x_ll) / (x_l - x_ll) * (y_l - y_ll) + y_ll, (10000 - x_ll) / (x_l - x_ll) * (y_l - y_ll) + y_ll])

print_line()
print_circle()
print_recctangle()

x, y = [x_l, x_ll], [y_l, y_ll]
line(x, y)

x = [min(x_rec, x_recc), min(y_rec, y_recc)]
rectangle(x, l_tangle, d_tangle)
x = [x_cer, y_cer]
circle(x, r_cer)
plt.gca().scatter(x_toh, y_toh)
plt.show()
