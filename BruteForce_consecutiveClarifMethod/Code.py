from math import *
import matplotlib.pyplot as plt
from numpy.core.multiarray import arange

N = 11
x_a = -N
x_b = N
H = 0.055


def F2(x_cur):
    return (x_cur - N / 2) ** 2 + N * x_cur


def F3(x_cur):
    return (x_cur - N / 2) ** 2 + N * (x_cur ** 2)


def F1(x_cur):
    return (x_cur - N / 2) ** 2


def drawGraphs(x, y1, y2, y3):
    plt.plot(x, y1, label='F1(x)', color='red')
    plt.plot(x, y2, label='F2(x)', color='blue')
    plt.plot(x, y3, label='F3(x)', color='black')
    plt.grid()
    plt.xlabel('Значення аргумента')
    plt.ylabel('Значення функції')
    plt.legend()
    plt.show()


def bruteForceMethod(f, array_min):
    min = f(x_a)
    x_cur = x_a
    x_min = x_a
    while x_cur <= x_b:
        if f(x_cur) < min:
            min = f(x_cur)
            x_min = x_cur
        array_min.insert(i, min)
        x_cur = x_cur + H
    return x_min, min


def consecutiveСlarifMethod(f, x_min, f_min):
    min = f_min
    arr_x_min = []
    i = 0
    j = round(x_min - 1, 2)
    while j < x_min + 1:
        if f(j) < min:
            min = f(j)
        arr_x_min.insert(i, min)
        j = round(j + 0.1, 2)
        i = i + 1
    return arr_x_min


def Z(x_opt, x_min):
    z = []
    for i in range(20):
        z.insert(i, x_opt - x_min[i])
    return z


x_cur = x_a
h = (N * 2) / 20

x = []
f1 = []
f2 = []
f3 = []

i = 0
while x_cur <= x_b:
    x.insert(i, x_cur)
    f1.insert(i, F1(x_cur))
    f2.insert(i, F2(x_cur))
    f3.insert(i, F3(x_cur))
    i = i + 1
    x_cur = x_cur + h

plt.title('Графіки функцій')
drawGraphs(x, f1, f2, f3)

# Для перебору
arr_min_brute_f1 = []
x_min1, f_min1 = bruteForceMethod(F1, arr_min_brute_f1)
arr_min_brute_f2 = []
x_min2, f_min2 = bruteForceMethod(F2, arr_min_brute_f2)
arr_min_brute_f3 = []
x_min3, f_min3 = bruteForceMethod(F3, arr_min_brute_f3)
plt.title('Графіки функцій x_min(k) для алгоритму перебору')
drawGraphs(arange(-N, N + H, H), arr_min_brute_f1, arr_min_brute_f2, arr_min_brute_f3)

# Для послідовних уточнень
arr_min_up_f1 = []
arr_min_up_f1 = consecutiveСlarifMethod(F1, x_min1, f_min1)
plt.title('Графік функції x_min(k) 1 рівняння для алгоритму послідовного уточнення')
drawGraphs(arange(x_min1 - 1, x_min1 + 1, 0.1), arr_min_up_f1, arr_min_up_f1, arr_min_up_f1)

arr_min_up_f2 = []
arr_min_up_f2 = consecutiveСlarifMethod(F1, x_min2, f_min2)
plt.title('Графік функції x_min(k) 2 рівняння для алгоритму послідовного уточнення')
drawGraphs(arange(x_min1 - 1, x_min1 + 1, 0.1), arr_min_up_f2, arr_min_up_f2, arr_min_up_f2)

arr_min_up_f3 = []
arr_min_up_f3 = consecutiveСlarifMethod(F1, x_min3, f_min3)
plt.title('Графік функції x_min(k) 3 рівняння для алгоритму послідовного уточнення')
drawGraphs(arange(x_min1 - 1, x_min1 + 1, 0.1), arr_min_up_f3, arr_min_up_f3, arr_min_up_f3)

# Таблиці
print("Таблиця функції Xmin(k) для функції F1 (Алг. перебору)")
print(arr_min_brute_f1)
print("")
print("Таблиця функції Xmin(k) для функції F2 (Алг. перебору)")
print(arr_min_brute_f2)
print("")
print("Таблиця функції Xmin(k) для функції F3 (Алг. перебору)")
print(arr_min_brute_f3)
print("")
print("Таблиця функції Xmin(k) для функції F1 (Алг. послідовного уточнення)")
print(arr_min_up_f1)
print("")
print("Таблиця функції Xmin(k) для функції F2 (Алг. послідовного уточнення)")
print(arr_min_up_f2)
print("")
print("Таблиця функції Xmin(k) для функції F3 (Алг. послідовного уточнення)")
print(arr_min_up_f3)
print("")
