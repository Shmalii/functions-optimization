import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable

N = 11
xlist = [-1.2 * N, 1.5 * N]
eps = 0.001
k = 20


def f1(xlis):
    global N
    return (xlis[0] - N) ** 2 + (2 * xlis[1] - N) ** 2


def f2(xlis):
    global N
    return (10 * (3 * N * xlis[1] - xlis[0] ** 2) ** 2) + (N - xlis[0]) ** 2



def Golden_section_method(f, x_list, index):
    global N
    x_ah = -2 * N
    x_bh = 2 * N
    xtemplistp = list.copy(x_list)
    xtemplistq = list.copy(x_list)
    p1 = x_ah + 0.382 * (x_bh - x_ah)
    q1 = x_ah + 0.618 * (x_bh - x_ah)
    x = (p1 + q1) / 2
    for k in range(1, 21):
        if abs(x_bh - x_ah) > eps:
            xtemplistp[index] = p1
            xtemplistq[index] = q1
            # print(xtemplistp, '---', xtemplistq)
            if f(xtemplistp) > f(xtemplistq):
                x_ah = p1
                x_bh = x_bh
                p1 = q1
                q1 = x_ah + 0.618 * (x_bh - x_ah)
            else:
                x_ah = x_ah
                x_bh = q1
                q1 = p1
                p1 = x_ah + 0.382 * (x_bh - x_ah)
            x = (p1 + q1) / 2
        else:
            break
    return x


def CiclicDescent(xlis, f):
    global k, eps
    ki = 0
    Xs = list.copy(xlis)
    Xlist = list(list())
    fl = 0
    fh = f(Xs)
    Xlist.append((Xs[0], Xs[1]))
    while ki <= k and abs(fh-fl) >= eps:
        for i in range(2):
            Xs[i] = Golden_section_method(f, list.copy(Xs), i)
            Xlist.append((Xs[0], Xs[1]))
        fl = fh
        fh = f((Xs[0], Xs[1]))
        ki += 1
    return Xlist


def CreateTable(f_list,f ,index):
    tablef = PrettyTable()
    fx1 = list()
    fx2 = list()
    for i in f_list:
        fx1.append(i[0])
        fx2.append(i[1])
    column_names1 = ["x1", "x2", "f{0}(x1, x2)".format(index)]
    tablef.add_column(column_names1[0], fx1)
    tablef.add_column(column_names1[1], fx2)
    tablef.add_column(column_names1[2], f)
    print(tablef)


def Create3Dfunc(index, f):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x, y = np.mgrid[-2 * N:2 * N:100j, -2 * N - 20:2 * N:100j]
    ax.set_title("F{0}".format(index))
    ax.set_xlabel("$x1$", fontsize=13)
    ax.set_ylabel("$x2$", fontsize=13)
    ax.set_zlabel("$F(x1,x2)$", fontsize=13)
    ax.plot_surface(x, y, f((x,y)), cmap='inferno')


def CreateFunction(f_list, index, f):
    fx1 = list()
    fx2 = list()
    for i in f_list:
        fx1.append(i[0])
        fx2.append(i[1])
    fig, ax = plt.subplots()
    ax.set_title("F{0}".format(index))
    ax.set_xlabel("x1")
    ax.set_ylabel("x2")
    ax.grid()
    ax.plot(fx1, fx2, c="green")
    ax.scatter(fx1, fx2, c="red")
    x, y = np.mgrid[-2 * N:2 * N:100j, -2 * N-20:2 * N:100j]
    ax.contour(x, y, f((x, y)), 20)
    plt.xlim(-2*N,2*N)
    plt.ylim(-2 * N, 2 * N)
    Create3Dfunc(index, f)


f1_list = dict ()
f2_list = dict()
f1l = list()
f2l = list()
f1x_list = CiclicDescent(list.copy(xlist), f1)
for i in f1x_list:
    f1_list[i] = f1(i)
    f1l.append(f1_list[i])
f2x_list = CiclicDescent(list.copy(xlist), f2)
for i in f2x_list:
    f2_list[i] = f2(i)
    f2l.append(f2_list[i])
print(f2((11,11/3)))
CreateTable(f1x_list, f1l,1)
CreateTable(f2x_list,f2l, 2)
print(f1x_list)
print(f2x_list)
CreateFunction(f1_list, 1, f1)
CreateFunction(f2_list, 2, f2)
plt.show()
