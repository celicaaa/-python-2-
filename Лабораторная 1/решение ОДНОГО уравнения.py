from math import *
from tkinter import *
import scipy
import os
import matplotlib.pyplot as plt

win = Tk()
win.geometry('1100x600')
win.title('Лабораторная работа 1')
Label(win, text='Начало отрезка', font='Times_New_Roman 10', bg='rosybrown', width=20).grid(row=0, column=0)
Label(win, text='Конец отрезка', font='Times_New_Roman 10', bg='rosybrown', width=20).grid(row=0, column=1)
Label(win, text='Точность', font='Times_New_Roman 10', bg='rosybrown', width=20).grid(row=0, column=2)

Label(win, text='Метод', fg='OrangeRed4', font='Times_New_Roman 10').grid(row=3, column=0, padx=10, pady=20)
Label(win, text='Метод деления', font='Times_New_Roman 10', fg='OrangeRed4').grid(row=4, column=0, padx=10, pady=20,)
Label(win, text='Метод касательных', font='Times_New_Roman 10', fg='OrangeRed4').grid(row=5, column=0, padx=10,pady=20)
Label(win, text='Метод хорд', font='Times_New_Roman 10', fg='OrangeRed4').grid(row=6, column=0, padx=10, pady=20)
Label(win, text='Метод касательных', font='Times_New_Roman 10', fg='OrangeRed4').grid(row=5, column=0, padx=10, pady=20)
Label(win, text='Метод итераций', font='Times_New_Roman 10', fg='OrangeRed4').grid(row=7, column=0, padx=10, pady=20,)
Label(win, text='Корень', font='Times_New_Roman 10', fg='OrangeRed4').grid(row=3, column=1, padx=10, pady=20)
Label(win, text='Кол-во итераций', font='Times_New_Roman 10', fg='OrangeRed4').grid(row=3, column=2, padx=10, pady=20)
Label(win, text='Scipy', font='Times_New_Roman 10', fg='OrangeRed4').grid(row=3, column=3, padx=10, pady=20)
Label(win,text='Исходное выражение: 2**x + 5*x - 3', font='Times_New_Roman 10', fg='OrangeRed4').grid(row=5, column=8,padx=10, pady=20)

aEntry = Entry(font='Times_New_Roman 10', width=8)
aEntry.grid(row=1, column=0)
bEntry = Entry(font='Times_New_Roman 10', width=8)
bEntry.grid(row=1, column=1)
epsEntry = Entry(font='Times_New_Roman 10', width=8)
epsEntry.grid(row=1, column=2)


# Нахождение корней
def f(x):
    a = 2*sin(x+pi/3)-0.5*x**2+1
    return a


def f1(x):
    a = log(2)*2**x+5
    return a


def f2(x):
    a = log(2)**2*2**x
    return a


# Метод деления
def delkr(a, b, eps, i):
    i += 1
    if f(a) * f(b) < 0:
        x = (a + b) / 2
        if abs(f(x)) < eps:
            return x, i
        else:
            if f(a) * f(x) < 0:
                return delkr(a, x, eps, i)
            else:
                return delkr(x, b, eps, i)


# Метод касательных
def kas(a, b, eps, i):
    i += 1
    x0 = (a + b) / 2
    xn = f(x0)
    xn1 = xn - f(xn) / f1(xn)
    while abs(xn1 - xn) > eps:
        xn = xn1
        xn1 = xn - f(xn) / f1(xn)
    return xn1, i


# Метод хорд
def hord(a, b, eps, i):
    i += 1
    x = a - (f(a) * (b - a) / (f(b) - f(a)))
    if abs(f(x)) <= eps:
        return x, i
    else:
        if f(a) * f2(x) > 0:
            return hord(a, x, eps, i)
        else:
            return hord(x, b, eps, i)


# Метод итераций
def itr(x, eps, i):
    i += 1
    f = 2**x + 5*x - 3
    if abs(f) <= eps:
        return x, i
    else:
        x = x - f / (2**x * log(2) + 5)
        return itr(x, eps, i)


def CalculateAll():
    a = float(aEntry.get())
    b = float(bEntry.get())
    eps = float(epsEntry.get())
    z1, t1 = delkr(a, b, eps, 0)
    Label(text=("{:.3f}".format(z1)), font='Times_New_Roman 10').grid(row=4, column=1, padx=10, pady=20, sticky='S')
    Label(text=t1, font='Times_New_Roman 10').grid(row=4, column=2, padx=10, pady=20, sticky='S')
    z2, t2 = kas(a, b, eps, 0)
    Label(text=("{:.3f}".format(z2)), font='Times_New_Roman 10').grid(row=5, column=1, padx=10, pady=20, sticky='S')
    Label(text=t2, font='Times_New_Roman 10').grid(row=5, column=2, padx=10, pady=20, sticky='S')
    z3, t3 = hord(a, b, eps, 0)
    Label(text=("{:.3f}".format(z3)), font='Times_New_Roman 10').grid(row=6, column=1, padx=10, pady=20, sticky='S')
    Label(text=t3, font='Times_New_Roman 10').grid(row=6, column=2, padx=10, pady=20, sticky='S')
    z4, t4 = itr(a, eps, 0)
    Label(text=("{:.3f}".format(z4)), font='Times_New_Roman 10').grid(row=7, column=1, padx=10, pady=20, sticky='S')
    Label(text=t4, font='Times_New_Roman 10').grid(row=7, column=2, padx=10, pady=20, sticky='S')

    sci1 = Entry(font='Times_New_Roman 10', width=15)
    sci1.grid(row=4, column=3)
    sci2 = Entry(font='Times_New_Roman 10', width=15)
    sci2.grid(row=5, column=3)
    sci3 = Entry(font='Times_New_Roman 10', width=15)
    sci3.grid(row=6, column=3)
    sci4 = Entry(font='Times_New_Roman 10', width=15)
    sci4.grid(row=7, column=3)

    sci1.configure(state='normal')
    sci1.delete(0, END)
    sci1.insert(0, '{:.3f}'.format(scipy.optimize.bisect(f, a, b)))
    sci1.configure(state='readonly')

    sci2.configure(state='normal')
    sci2.delete(0, END)
    sci2.insert(0, scipy.optimize.root_scalar(f, x0=a, x1=b, method='secant').root)
    sci2.configure(state='readonly')

    sci3.configure(state='normal')
    sci3.delete(0, END)
    sci3.insert(0, '{:.3f}'.format(scipy.optimize.newton(f, a)))
    sci3.configure(state='readonly')

    sci4.configure(state='normal')
    sci4.delete(0, END)
    sci4.insert(0, '{:.3f}'.format(scipy.optimize.ridder(f, a, b)))


def grafik():
    k = -5
    v = []
    u = []
    while k < 5:
        v.append(k)
        u.append(f(k))
        k += 0.002
    plt.plot(v, u, 'b--')
    plt.grid(True)
    plt.xlabel(r'$x$', fontsize=10)
    plt.ylabel(r'$f(x)$', fontsize=10)
    v1 = []
    u1 = []
    for i in range(len(u) - 1):
        if u[i] * u[i + 1] < 0:
            v1.append(v[i + 1])
            u1.append(u[i + 1])
    plt.scatter(v1, u1, marker='o', color='r', s=50)
    plt.show()


calculateButton = Button(text="Вычислить", font='Times_New_Roman 10', command=CalculateAll).grid(row=1, column=7)
bt2 = Button(text='График', font='Times_New_Roman 10', command=grafik).grid(row=1, column=8)
win.mainloop()