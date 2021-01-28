# -*- coding: utf-8 -*-
from math import *
import unicodedata
import matplotlib.pyplot as plt
from numpy.core.multiarray import arange
from prettytable import PrettyTable

N = 11
x_a = -N
x_b = 3 * N
n = 20
eps = 0.001
liambda = 0.0001
Z_opt1 = []
Z_opt2 = []
Z_opt3 = []
F_opt1 = 0
F_opt2 = -151.25
F_opt3 = 110.9167

def F2(x_cur):
    return (x_cur - N) ** 2 - N * x_cur


def F3(x_cur):
    return (x_cur - N) ** 2 + N * x_cur*x_cur


def F1(x_cur):
    return (x_cur - N) ** 2


def Half_divide_method(f, x_list, f_list):
    global x_a, x_b
    x_ah = x_a
    x_bh = x_b
    for k in range(1, 21):
        if fabs(x_bh - x_ah) >= eps:
            p = (x_bh + x_ah) / 2 - liambda
            q = (x_bh + x_ah) / 2 + liambda
            x = (x_bh + x_ah) / 2
            x_ah, x_bh = (x_ah, q) if f(p) < f(q) else (p, x_bh)
            x_list.append(x)
            f_list.append(f(x))
    return x_list, f_list


def Golden_section_method(f, x_list, f_list):
    global x_a, x_b
    x_ah= x_a
    x_bh = x_b
    p1 = x_ah + 0.382 * (x_bh - x_ah)
    q1 = x_ah + 0.618 * (x_bh - x_ah)
    for k in range(1, 21):
        if fabs(x_bh - x_ah) >= eps:
            if f(p1) > f(q1):
                x_ah = p1
                x_bh = x_bh
                p1 = q1
                q1 = x_ah+0.618*(x_bh - x_ah)
            else:
                x_ah = x_ah
                x_bh = q1
                q1 = p1
                p1 = x_ah+0.382*(x_bh - x_ah)
            x = (p1+q1)/2
            f_list.append(f(x))
            x_list.append(x)
        else:
            f_list.append(0)
            x_list.append(0)
    return x_list, f_list


def call_f(f, F):
    x1_list = list()
    f1_list = list()
    x1_list, f1_list = f(F, x1_list, f1_list)
    min1 = F(x1_list[0])
    x_min = 0
    for elem in x1_list:
        if min1 >= F(elem):
            min1 = F(elem)
            x_min = elem
    print(min1)
    print(x_min)
    print(f1_list)


F1_hdm = []
F1_x_hdm = []
F1_x_hdm, F1_hdm = Half_divide_method(F1,F1_x_hdm,F1_hdm)
F2_hdm = list()
F3_hdm = list()
F2_x_hdm = list()
F3_x_hdm = list()
F2_x_hdm, F2_hdm = Half_divide_method(F2,F2_x_hdm,F2_hdm)
F3_x_hdm, F3_hdm = Half_divide_method(F3,F3_x_hdm,F3_hdm)
F1_gsm = list()
F2_gsm = list()
F3_gsm = list()
F1_x_gsm = list()
F2_x_gsm = list()
F3_x_gsm = list()
F1_x_gsm, F1_gsm = Golden_section_method(F1,F1_x_gsm,F1_gsm)
F2_x_gsm, F2_gsm = Golden_section_method(F2,F2_x_gsm,F2_gsm)
F3_x_gsm, F3_gsm = Golden_section_method(F3,F3_x_gsm,F3_gsm)
print("Таблиця значень  для дихотомічного пошуку")
k_mas = []
for i in range(1,21):
    k_mas.append(i)
k_mas1 = []
for i in range(1,17):
    k_mas1.append(i)
table1 = PrettyTable()
column_names1 = ["k", "X1min(k)", "F1(X1min(k))", "X2min(k)", "F2(X2min(k))", "X3min(k)", "F3(X3min(k))"]
table1.add_column(column_names1[0], k_mas1)
table1.add_column(column_names1[1], F1_x_hdm)
table1.add_column(column_names1[2], F1_hdm)
table1.add_column(column_names1[3], F2_x_hdm)
table1.add_column(column_names1[4], F2_hdm)
table1.add_column(column_names1[5], F3_x_hdm)
table1.add_column(column_names1[6], F3_hdm)
print(table1)
print("Таблиця значень для методу золотого перерізу")
table2 = PrettyTable()
column_names1 = ["k", "X1min(k)", "F1(X1min(k))", "X2min(k)", "F2(X2min(k))", "X3min(k)", "F3(X3min(k))"]
table2.add_column(column_names1[0], k_mas)
table2.add_column(column_names1[1], F1_x_gsm)
table2.add_column(column_names1[2], F1_gsm)
table2.add_column(column_names1[3], F2_x_gsm)
table2.add_column(column_names1[4], F2_gsm)
table2.add_column(column_names1[5], F3_x_gsm)
table2.add_column(column_names1[6], F3_gsm)
print(table2)
plt.plot(F3_x_hdm,label='Метод ділення навпіл', color="red")
plt.plot(F3_x_gsm, label='Метод золотого перетину', color="green")
plt.title('Мінімуми Xmin(k) для F3')
plt.xlabel('Ітерація')
plt.ylabel('Значення Xmin(k)')
plt.legend()
plt.grid()
plt.show()


def Z(x_opt, x_min):
    z = []
    for i in range(len(x_min)):
        z.insert(i, fabs(x_opt - x_min[i]))
    return z


Z_opt1_hdm = []
Z_opt2_hdm = []
Z_opt3_hdm = []
Z_opt1_hdm=Z(F_opt1, F1_hdm)
Z_opt2_hdm=Z(F_opt2, F2_hdm)
Z_opt3_hdm=Z(F_opt3, F3_hdm)
Z_opt1_gsm = []
Z_opt2_gsm= []
Z_opt3_gsm = []
Z_opt1_gsm=Z(F_opt1, F1_gsm)
Z_opt2_gsm=Z(F_opt2, F2_gsm)
Z_opt3_gsm=Z(F_opt3, F3_gsm)
table3 = PrettyTable()
column_names = ["k", "Z1(k)", "Z2(k)", "Z3(k)"]
table3.add_column(column_names[0], k_mas[0:16])
table3.add_column(column_names[1], Z_opt1_hdm)
table3.add_column(column_names[2], Z_opt2_hdm)
table3.add_column(column_names[3], Z_opt3_hdm)
print(table3)
plt.plot(Z_opt1_hdm,label='Метод ділення навпіл F1', color="black")
plt.plot(Z_opt1_gsm, label='Метод золотого перетину F1', color="blue")
plt.plot(Z_opt2_hdm,label='Метод ділення навпіл F2', color="purple")
plt.plot(Z_opt2_gsm, label='Метод золотого перетину F2', color="pink")
plt.plot(Z_opt3_hdm,label='Метод ділення навпіл F3', color="red")
plt.plot(Z_opt3_gsm, label='Метод золотого перетину F3', color="green")
plt.title('Zopt123(k)')
plt.xlabel('Ітерація')
plt.ylabel('Значення Zopt(k)')
plt.legend()
plt.grid()
plt.show()