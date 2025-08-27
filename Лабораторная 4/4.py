from math import *
from tkinter import *
import os

root = Tk()
root.title("lab4")
root.geometry("1800x800")
root.configure(background='rosybrown')

h = PhotoImage(file="4.png")

lbk = Label(root)
lbk.image = h
lbk['image'] = lbk.image
lbk.place(x=400, y=40)



la = Label(root, text="введите A", font=('Arial', 14))
la.place(x=72, y=30)
eda = Entry(root, font=('Arial', 14), width=10)
eda.place(x=66, y=60)

lb = Label(root, text="введите B", font=('Arial', 15))
lb.place(x=72, y=90)
edb = Entry(root, font=('Arial', 15), width=10)
edb.place(x=66, y=120)


def f(x):
    return x/(1+x**2)


X = [ 0, 0.31, 0.63, 0.94, 1.26, 1.57, 1.57, 1.88, 2.2, 2.36, 2.51, 2.83, 3.14]
Y = [0.15, 0.153, 0.163, 0.18, 0.208, 0.25, 0.314, 0.409, 0.538, 0.674, 0.738]


def levie():
    a = float(eda.get())
    b = float(edb.get())
    e = 0.001

    s = 0
    n = int(abs(b - a) // e + 1)

    for i in range(n):
        s = s + e * f(a)
        a += e

    l = Label(root, text="X = ", font=('Arial', 15),bg='LightCyan2')
    l.place(x=400, y=300)
    lx = Label(root, text=s, font=('Arial', 15),bg='LightCyan2')
    lx.place(x=450, y=300)


def srednie():
    a = float(eda.get())
    b = float(edb.get())
    e = 0.001

    s = 0
    n = int(abs(b - a) // e + 1)

    a = a + e / 2

    for i in range(n):
        s = s + e * f(a)
        a += e

    l = Label(root, text="X = ", font=('Arial', 15),bg='LightCyan2')
    l.place(x=400, y=350)
    lx = Label(root, text=s, font=('Arial', 15),bg='LightCyan2')
    lx.place(x=450, y=350)


def pravie():
    a = float(eda.get())
    b = float(edb.get())
    e = 0.001

    s = 0
    n = int(abs(b - a) // e + 1)

    for i in range(1, n + 1):
        s = s + e * f(a)
        a += e

    l = Label(root, text="X = ", font=('Arial', 15),bg='LightCyan2')
    l.place(x=400, y=400)
    lx = Label(root, text=s, font=('Arial', 15),bg='LightCyan2')
    lx.place(x=450, y=400)


def trapecii():
    a = float(eda.get())
    b = float(edb.get())
    e = 0.001

    s = e * f(a) / 2
    n = int(abs(b - a) // e + 1)

    for i in range(1, n - 1):
        a += e
        s += e * f(a)

    a += e
    s += e * f(a) / 2

    l = Label(root, text="X = ", font=('Arial', 15),bg='LightCyan2')
    l.place(x=400, y=450)
    lx = Label(root, text=s, font=('Arial', 15),bg='LightCyan2')
    lx.place(x=450, y=450)


def simpson():
    a = float(eda.get())
    b = float(edb.get())
    e = 0.001

    s = (e / 3) * (f(a) + f(b))
    n = int(abs(b - a) // e + 1)

    for i in range(1, n - 1):
        a = a + e
        if i % 2 == 0:
            s += (e / 3) * 4 * (f(a))
        else:
            s += (e / 3) * 2 * (f(a))

    l = Label(root, text="X = ", font=('Arial', 15),bg='LightCyan2')
    l.place(x=400, y=500)
    lx = Label(root, text=s, font=('Arial', 15),bg='LightCyan2')
    lx.place(x=450, y=500)

def analys():
    an = log(2)/2
    l = Label(root, text="X = ", font=('Arial', 15),bg='LightCyan2')
    l.place(x=400, y=550)
    lx = Label(root, text=an, font=('Arial', 15),bg='LightCyan2')
    lx.place(x=450, y=550)

def file():
    os.startfile('oaoa4.xlsm')

btn1 = Button(root, text="Левые треугольники", font="bold 14", command=levie, relief=RAISED)
btn1.place(x=65, y=300)

btn2 = Button(root, text="Средние треугольники", font="bold 14", command=srednie, relief=RAISED)
btn2.place(x=65, y=350)

btn3 = Button(root, text="Правые треугольники", font="bold 14", command=pravie, relief=RAISED)
btn3.place(x=65, y=400)

btn4 = Button(root, text="Метод трапеций", font="bold 14", command=trapecii, relief=RAISED)
btn4.place(x=65, y=450)

btn5 = Button(root, text="Метод Симпсона", font="bold 14", command=simpson, relief=RAISED)
btn5.place(x=65, y=500)

btn6 = Button(root, text = "Аналитическое решение",command=analys, font="bold 14", relief=RAISED)
btn6.place(x=65, y=550)

btn7 = Button(root, text = "Excel", command=file,  font="bold 14", relief=RAISED)
btn7.place(x=65, y=600)

root.mainloop()