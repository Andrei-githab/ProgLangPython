import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
import keyboard
plt.figure(figsize=(8, 8))
plt.gca().spines['left'].set_position('center')
plt.gca().spines['bottom'].set_position('center')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)


def line(x1_line, x2_line):
    plt.plot(x1_line, x2_line, color="k")


def rectangle(x_rectangle, l, d):
    currentAxis = plt.gca()
    currentAxis.add_patch(Rectangle((x_rectangle), l, d, facecolor="None", ec='k'))


def circle(x,r):
    circle1 = plt.Circle((x), r, color='None', ec='k')
    plt.gca().add_patch(circle1)




x1,y1,x2,y2 = map(int,input().split())
x3, y3, x4, y4 = map(int,input().split())
x5, y5, r = map(int,input().split())
x6,y6 = map(int,input().split())
plt.xlim(min(x1,x2,x3,x4,x5-r,x6,y1,y2,y3,y4,y5-r,y6,-x1,-x2,-x3,-x4,-(x5-r),-x6,-y1,-y2,-y3,-y4,-(y5-r),-y6,y5+r,y5-r,-y5-r,-y5+r)-3, max(x1,x2,x3,x4,x5-r,x6,y1,y2,y3,y4,y5-r,y6,-x1,-x2,-x3,-x4,-(x5-r),-x6,-y1,-y2,-y3,-y4,-(y5-r),-y6,y5+r,y5-r,-y5-r,-y5+r)+3)
plt.ylim(min(x1,x2,x3,x4,x5-r,x6,y1,y2,y3,y4,y5-r,y6,-x1,-x2,-x3,-x4,-(x5-r),-x6,-y1,-y2,-y3,-y4,-(y5-r),-y6,y5+r,y5-r,-y5-r,-y5+r)-3, max(x1,x2,x3,x4,x5-r,x6,y1,y2,y3,y4,y5-r,y6,-x1,-x2,-x3,-x4,-(x5-r),-x6,-y1,-y2,-y3,-y4,-(y5-r),-y6,y5+r,y5-r,-y5-r,-y5+r)+3)

plt.gca().add_patch(Rectangle((-10000,-10000), 20000, 20000, facecolor="cyan"))
l = max(x3,x4)-min(x3,x4)
d = max(y3,y4)-min(y3,y4)


def print_circle():

    ra = (x6-x5)*(x6-x5)+(y6-y5)*(y6-y5)

    if r*r < ra:
        plt.gca().add_patch(plt.Circle([x5,y5], r, color='w',))
    else:
        plt.gca().add_patch(Rectangle((-10000,y5+r), 20000, 20000, facecolor="w"))
        plt.gca().add_patch(Rectangle((-10000,y5-r), 20000, -20000, facecolor="w"))
        plt.gca().add_patch(Rectangle((x5+r,y5+r), 20000, -20000, facecolor="w"))
        plt.gca().add_patch(Rectangle((x5-r,y5-r), -20000, 20000, facecolor="w"))
        xp = np.array([x5-r,x5-r*0.98,x5-r*0.96,x5-r*0.94,x5-r*0.92,x5-r*0.9,x5-r*0.8,x5-r*0.7,x5-r*0.6,x5-r*0.5,x5-r*0.4,x5-r*0.3,x5-r*0.2,x5-r*0.1,x5,x5+r*0.1,x5+r*0.2,x5+r*0.3,x5+r*0.4,x5+r*0.5,x5+r*0.6,x5+r*0.7,x5+r*0.8,x5+r*0.9,x5+r*0.92,x5+r*0.94,x5+r*0.96,x5+r*0.98,x5+r])
        yp = np.array([y5,y5+r*0.2,y5+r*0.28,y5+r*0.34,y5+r*0.4,y5+r*0.43,y5+r*0.6,y5+r*0.71,y5+r*0.8,y5+r*0.86,y5+r*0.91,y5+r*0.95,y5+r*0.98,y5+r*0.99,y5+r,y5+r*0.99,y5+r*0.98,y5+r*0.95,y5+r*0.91,y5+r*0.86,y5+r*0.8,y5+r*0.71,y5+r*0.6,y5+r*0.43,y5+r*0.4,y5+r*0.34,y5+r*0.28,y5+r*0.2,y5])
        plt.fill_between(xp,yp,y2=y5+r,color = "w")
        yp = np.array(
            [y5, y5 - r * 0.2, y5 - r * 0.28, y5 - r * 0.34, y5 - r * 0.4, y5 - r * 0.43, y5 - r * 0.6, y5 - r * 0.71,
             y5 - r * 0.8, y5 - r * 0.86, y5 - r * 0.91, y5 - r * 0.95, y5 - r * 0.98, y5 - r * 0.99, y5 - r,
             y5 - r * 0.99, y5 - r * 0.98, y5 - r * 0.95, y5 - r * 0.91, y5 - r * 0.86, y5 - r * 0.8, y5 - r * 0.71,
             y5 - r * 0.6, y5 - r * 0.43, y5 - r * 0.4, y5 - r * 0.34, y5 - r * 0.28, y5 - r * 0.2, y5])

        plt.fill_between(xp, yp, y2=y5 - r, color="w")


def print_line():
    
    if(x1!=x2):
        kx = (x1 - x2) / (y1 - y2)
        bx = -y2 * (x1 - x2) / (y1 - y2) + x2
        ky = (y1 - y2) / (x1 - x2)
        by = -x2 * (y1 - y2) / (x1 - x2) + y2
        if (y6!=x6*ky+by):
            if ((-1) - x2) / (x1 - x2) * (y1 - y2) + y2 < (- x2) / (x1 - x2) * (y1 - y2) + y2:
                if bx < 0:
                    if (y6 > x6 * ky + by):
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
                    if (y6 > x6 * ky + by):
                        plt.fill_betweenx([-10000, by], [-10000 * 1 / ky + by, 0], color="w")
                        plt.gca().add_patch(Rectangle((0, -10000), 10000, 10000, facecolor="w"))
                        plt.fill_between([bx, 0], [0, by], color="cyan")
                        plt.fill_between([bx, 10000], [0, 10000 * ky + by], color="w")
                    else:
                        plt.fill_between([-10000, bx], [-10000 * ky + by, 0], color="w")
                        plt.gca().add_patch(Rectangle((-10000, 10000), 10000, -10000, facecolor="w"))
                        plt.fill_between([bx, 0], [0, by], color="cyan")
                        plt.fill_betweenx([by, 10000], [0, 10000 * 1 / ky + by], color="w")

            elif ((-1) - x2) / (x1 - x2) * (y1 - y2) + y2 > (-x2) / (x1 - x2) * (y1 - y2) + y2:
                if bx < 0:
                    if (y6 > x6 * ky + by):
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
                    if (y6 > x6 * ky + by):
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
        if(x6 > x1):
            plt.gca().add_patch(Rectangle((x6, 10000), 20000, -20000, facecolor="w"))
        else:
            plt.gca().add_patch(Rectangle((x6, 10000), -20000, -20000, facecolor="w"))


def print_recctangle():

    if (min(x3, x4) <= x6 <= max(x3, x4)) and (min(y3, y4) <= y6 <= max(y3, y4)):

        plt.gca().add_patch(Rectangle((-10000, max(y3,y4)), 20000, 20000, facecolor="w"))
        plt.gca().add_patch(Rectangle((-10000, max(y3,y4)), min(x3,x4)+10000, -20000, facecolor="w"))
        plt.gca().add_patch(Rectangle((max(x3,x4), max(y3, y4)), 20000, -20000, facecolor="w"))
        plt.gca().add_patch(Rectangle((min(x3,x4), min(y3,y4)), 20000, -20000, facecolor="w"))
        print(1)
    else:
        plt.gca().add_patch(Rectangle(([min(x3, x4), min(y3, y4)]), l, d, facecolor="w"))
        print(2)


if x1 == x2:
    line([x1, x1], [-10000, 10000])
else:
    line([-10000, 10000], [(-10000-x2)/(x1-x2)*(y1-y2)+y2, (10000-x2)/(x1-x2)*(y1-y2)+y2])

print_line()
print_circle()
print_recctangle()

x, y = [x1, x2], [y1, y2]
line(x, y)

x = [min(x3, x4), min(y3, y4)]
rectangle(x, l, d)
x = [x5, y5]
circle(x, r)
plt.gca().scatter(x6, y6)
plt.show()
