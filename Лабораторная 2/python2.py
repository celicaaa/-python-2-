from tkinter import *
import matplotlib.pyplot as plt
from math import *
from numpy import *
from scipy.optimize import newton, fsolve, bisect
import os
from sympy import *
file = open("lab2.txt", "w")

root = Tk()
root.title('Лаб2')
root.geometry('1300x800')
root.configure(background='rosybrown')

img = PhotoImage(file='grafik.png')
im =Label(image=img)
im.place(x=20, y=20)

urav = PhotoImage(file = 'urav.png')
ur =Label(image=urav)
ur.place(x=20, y=450)

lx =Label(text='Введите значение x:')
lx.place(x=600, y=10)
lx1 =Entry(root)
lx1.place(x=845, y=10)

ly =Label(text='Введите значение y:')
ly.place(x=600, y=40)
ly1 =Entry(root)
ly1.place(x=845, y=40)

le = Label(text='Введите погрешность E:')
le.place(x=600, y=70)
le1 = Entry(root)
le1.insert(0, 0.001)
le1.place(x=845, y=70)


def f1(x, y): #1 уравнение
    return sin(y+1)-1.2*x-0.1


def f2(x, y): #2 уравнение
    return x**2+y**2-1


def fx(x, y): #выражение х из 1 уравнения
    return (sin(y+1)-0.1)/1.2


def fy(x, y): #выражение у из 2 уравения
    return (1 - x**2)**0.5
def fp1x(x, y):
    return -1.2
def fp1y(x, y):
    return cos(y+1)
def fp2x(x, y):
    return 2*x
def fp2y(x, y):
    return 2*y
def det(x, y):
    return fp1x(x, y) * fp2y(x, y) - fp1y(x, y) * fp2x(x, y)


def yakobi():
    x0 = float(lx1.get())
    y0 = float(ly1.get())
    e = float(le1.get())

    x = fx(x0, y0)
    y = fy(x0, y0)
    apx = []
    apy = []
    n = 0
    while (abs(x - x0) > e) and (abs(y - y0) > e):
        if n > 1000:
            file.write("Якоби:\n")
            file.write("Количество итераций: " + str(n))
            file.write("\nКорней нет")

            lb = Label(text='Корней нет')
            lb.place(x=600, y=390)
            return
        n += 1
        x0 = x
        y0 = y
        x = fx(x0, y0)
        y = fy(x0, y0)
        apx.append(x)
        apy.append(y)

    file.write("Якоби:\n")
    file.write("Количество итераций: " + str(n))
    file.write("\nКорни = " + str(x) + str(y))

    lbl1 = Label(text='Решение: ' + str(x) + ' ' + str(y))
    lbl1.place(x=600, y=390)
    lbl2 = Label( text='Приближение X: ' + str(apx))
    lbl2.place(x=600, y=415)
    lbl3 = Label(text='Приближение Y: ' + str(apy))
    lbl3.place(x=600, y=440)
    lbl4 = Label(text='Количество итераций: ' + str(n))
    lbl4.place(x=600, y=465)
    return x, y, n


def gss():
    x = float(lx1.get())
    y = float(ly1.get())
    e = float(le1.get())

    x0 = fx(x, y)
    y0 = fy(x0, y)
    apx = []
    apy = []
    n = 0

    while (abs(y - y0) > e) and (abs(x - x0)):
        if n > 1000:
            file.write("Гаусса-Зейделя:\n")
            file.write("Количество итераций: " + str(n))
            file.write("\nКорней нет")

            lb =Label(text='Корней нет', font=('Arial', 12), fg='turquoise1', bg='white')
            lb.place(x=600, y=545)
            return
        x = x0
        y = y0
        x0 = fx(x, y)
        y0 = fy(x0, y)
        n += 1
        apx.append(x)
        apy.append(y)

    file.write("Гаусса-Зейделя:\n")
    file.write("Количество итераций: " + str(n))
    file.write("\nКорни = " + str(x) + ' ' + str(y))

    lbl5 =Label(text='Решение: ' + str(x) + ' ' + str(y))
    lbl5.place(x=600, y=540)
    lbl6 = Label(text='Приближение Х: ' + str(apx))
    lbl6.place(x=600, y=565)
    lbl7 = Label(text='Приближение Y: ' + str(apy))
    lbl7.place(x=600, y=590)
    lbl8 =Label(text='Количество итераций: ' + str(n))
    lbl8.place(x=600, y=615)

def nwtn():
    x = float(lx1.get())
    y = float(ly1.get())
    e = float(le1.get())
    n = 1
    x1=f1(x, y)
    y1=f2(x, y)
    while abs(x1) > e and abs(y1) > e:
        n+= 1
        x1 = (fp1y(x, y) * f2(x, y) - fp2y(x, y) * f1(x, y)) / det(x, y)
        y1 = -(f1(x, y) + fp1x(x, y) * x1) / fp1y(x, y)
        x += x1
        y += y1
    lbl9 = Label( text='Решение: ' + str(x)+' ' + str(y))
    lbl9.place(x=600, y=690)
    lbl8 = Label(text='Количество итераций: ' + str(n))
    lbl8.place(x=600, y=715)
    return x, y, n

def file2():
    os.startfile('excel2.xlsx')

btn1 =Button(text='Метод Якоби', command=yakobi)
btn1.place(x=600, y=350)
btn2 =Button(text='Метод Гаусса-Зейделя', command=gss)
btn2.place(x=600, y=500)
btn3 = Button(text='Метод Ньютона', command=nwtn)
btn3.place(x=600, y=650)
btn4 = Button(text='Excel', command=file2)
btn4.place(x=600, y=200)
root.mainloop()
file.close()