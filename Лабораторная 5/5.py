from tkinter import *
from math import *
import matplotlib.pyplot as plt
import scipy.optimize
import numpy as np
import os


def f(x):
    return log(cos(x / exp(2)))


def fpl(x, n, kf):
    y = 0
    for i in range(n + 1):
        y += (x ** (n - i)) * float(kf[i])
    return y


def gau(a):
    for k in range(len(a) - 1):
        if float(a[k][k]) != 0:
            for i in range(k, len(a) - 1):
                m = float(a[i + 1][k]) / float(a[k][k])
                for j in range(len(a[i])):
                    a[i + 1][j] = float(a[i + 1][j]) - m * float(a[k][j])
    for k in range(len(a) - 1, -1, -1):
        if float(a[k][k]) != 0:
            m = float(a[i][k]) / float(a[k][k])
            for j in range(len(a[i])):
                a[i][j] = float(a[i][j]) - m * float(a[k][j])
    ans = [0] * len(a)
    return a, ans


def pln(a, b, n):
    mt1 = []
    for i in range(n + 1):
        mt1.append([1])
        for j in range(n):
            mt1[i].append(1)
    h = abs(a - b) / n
    zn1 = []

    for i in range(n + 1):
        zn1.append(a)
        a += h
    for i in range(n + 1):
        for j in range(n + 1):
            mt1[i][j] = zn1[i] ** (n - j)
    for i in range(n + 1):
        mt1[i].append(f(zn1[i]))
    for i in range(n):
        if mt1[i][i] == 0:
            mt1[i], mt1[i + 1] = mt1[i + 1], mt1[i]
    an, ans = gau(mt1)

    k = -1
    u = []
    v = []
    while k < b:
        v.append(k)
        u.append(fpl(k, n, ans))
        k += 0.1
    plt.scatter(v, u, s=25)
    plt.plot(v, u)
    plt.grid(True)
    plt.xlabel(r'$x$', fontsize=16)
    plt.xlabel(r'$f(x)$', fontsize=16)
    plt.show
    return ans


def vuvod():
    a = float(en1.get())
    b = float(en2.get())
    n = int(en3.get())

    otv1 = pln(a, b, n)
    otv = 'y='
    for i in range(len(otv1)):
        if i != 0:
            if len(otv1) - i - 1 == 0:
                if float(otv1[i]) > 0:
                    otv += '+' + otv1[i]
                elif float(otv1[i]) < 0:
                    otv += otv1[i]
            elif float(otv1[i]) > 0:
                otv += '+' + otv1[i] + '*' + 'x^' + str(len(otv1) - i - 1)
            elif float(otv1[i]) < 0:
                otv += otv1[i] + '*' + 'x^' + str(len(otv1) - i - 1)
            else:
                pass
        else:
            otv += otv1[i] + '*' + 'x^' + str(len(otv1) - i - 1)

    urav.configure(state='normal')
    urav.delete(0, END)
    urav.insert(0, otv)
    urav.configure(state='readonly')

    xx = np.linspace(40, 43, n=10)
    yy = (log(cos(xx / exp(2))))
    zn2 = np.polyfit(xx, yy, n)
    p2 = np.poly1d(z2)
    p2 = str(p2)


k = -1
u = []
v = []
while k < 4:
    v.append(k)
    u.append(f(k))
    k += 0.1
plt.scatter(v, u, s=25)
plt.plot(v, u)
plt.grid(True)
plt.xlabel(r'$x$', fontsize=16)
plt.xlabel(r'$f(x)$', fontsize=16)
plt.show()

root = Tk()
root.geometry('1400x800')
root.resizable(0, 0)
# img = PhotoImage(file='gr.png')
# im = Label(image=img, padx=20)
# im.grid(row=3, column=4, rowspan=8, sticky=N, pady=(60, 10), padx=(10, 10))

Label(text='Niz', font='Arial 12 bold', padx=10, pady=10).grid(row=0, column=0)
Label(text='verh', font='Arial 12 bold', padx=10, pady=10).grid(row=0, column=1)
Label(text='step', font='Arial 12 bold', padx=10, pady=10).grid(row=0, column=2)

pl_lb = Label(text='polinom', font='Arial 12 bold', padx=10)
pl_lb.grid(row=2, column=2, sticky=W)

md_lb1 = Label(text='poly1d', font='Arial 12 bold', padx=10)
md_lb1.grid(row=3, column=0, pady=(10, 10), sticky=W)

urav = Entry(font='Arial 12 bold', width=18)
urav.grid(row=2, column=0, padx=10)
uravpl = Label(font='Arial 12 bold', width=18)
uravpl.grid(row=3, column=1, sticky=W, columnspan=4, pady=(10, 10))

en1 = Entry(font='Arial 12 bold', width=18)
en1.grid(row=1, column=0, padx=10)
en2 = Entry(font='Arial 12 bold', width=18)
en2.grid(row=1, column=1, padx=10)
en3 = Entry(font='Arial 12 bold', width=18)
en3.grid(row=1, column=2, padx=10)

Button(text='Вычислить', font='Arial 12 bold', padx=20, width=10, command=vuvod).grid(row=5, column=0, pady=(30, 10))

root.mainloop()