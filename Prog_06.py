"""
Лабораторная работа 6
Напишите функцию, которая по веденному натуральному числу n возвращает n-e число Фибоначчи.
В этой задаче нельзя использовать циклы
"""

import sys

sys.setrecursionlimit(1600)


def getFibonacci(ceslofib):
    if ceslofib > 1:
        return getFibonacci(ceslofib - 1) + getFibonacci(ceslofib - 2)
    return ceslofib


print("############ Число Фибоначчи? ############\n")
print("Текущие параметры лимита глубины рекурсии:", end=' ')
print(sys.getrecursionlimit())
element = int(input('Введите номер искомого элемента: '))
print(str(element) + ' элемент последовательности равен ' + str(getFibonacci(element)))
