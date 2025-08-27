from tkinter import *
from numpy import *
import matplotlib.pyplot as plt
import math
from PIL import Image, ImageTk

root = Tk()
root.title("РГР 2, Астраханкина")
root.geometry("1200x650")
root.config(bg='MistyRose3')

Label(root,text='Границы первого корня',bg='#9D81BA').place(x=20,y=40)
A1=Entry(root,width=5)
A1.insert(0,'-2')
A1.place(x=40,y=70)
A2=Entry(root,width=5)
A2.insert(0,'-1')
A2.place(x=100,y=70)
Label(root,text='Границы второго корня',bg='#9D81BA').place(x=20,y=110)
B1=Entry(root,width=5)
B1.insert(0,'-1')
B1.place(x=40,y=140)
B2=Entry(root,width=5)
B2.insert(0,'0')
B2.place(x=100,y=140)
Label(root,text='Границы третьего корня',bg='#9D81BA').place(x=20,y=180)
C1=Entry(root,width=5)
C1.insert(0,'2')
C1.place(x=40,y=210)
C2=Entry(root,width=5)
C2.insert(0,'4')
C2.place(x=100,y=210)

def f(x):
    return 2*x**3-3*x**2-12*x-5

def df(x):
    return 6*x**2-6*x-12

def chord_method(a, b, tol):
    while abs(b-a) > tol:
        a = b - (b-a)*f(b)/(f(b)-f(a))
        b = a - (a-b)*f(a)/(f(a)-f(b))
    return b

def a():
    a1 = float(A1.get())
    a2 = float(A2.get())
    b1 = float(B1.get())
    b2 = float(B2.get())
    c1 = float(C1.get())
    c2 = float(C2.get())
    a = chord_method(a1, a2, 0.001)
    b = chord_method(b1, b2, 0.001)
    c = chord_method(c1, c2, 0.001)

    result_label1 = Label(root, text='Комбинированный метод хорд и касательных', font='Courier 13').place( x=185, y=90)
    result_label2 = Label(root, text=f" х1= {a:.3f}, x2 = {b:.3f}, x3 = {c:.3f}", font='Courier 11').place(x=185, y=120)

    img1 = Image.open('задание1.png')
    img1 = ImageTk.PhotoImage(img1)
    img_lable1 = Label(root, image=img1)
    img_lable1.image = img1
    img_lable1.place(x=700, y=100)

def calculate_integral():
    a = 0.6
    b = 2.4
    n1 = 9
    n2 = 12

    def f(x):
        return (1+0.5*x**2)/(1+(0.8*x**2+1.4)**0.5)

    def trapezoidal_rule(func, a, b, n):
        h = (b - a) / n
        result = 0.5 * (func(a) + func(b))
        for i in range(1, n):
            result += func(a + i * h)
        result *= h
        return result

    result_n1 = trapezoidal_rule(f, a, b, n1)
    result_n2 = trapezoidal_rule(f, a, b, n2)

    result_label8 = Label(root, text='Формула "трех восьмых" для интеграла', font='Courier 13').place(x=30, y=300)
    result_label3 = Label(root, text=f"При n=9: {result_n1:.5f}", font='Courier 11').place(x=30,y=330)
    result_label4 = Label(root, text=f"При n=12: {result_n2:.5f}", font='Courier 11').place(x=30, y=360)

    img2 = Image.open('задание2.png')
    img2 = ImageTk.PhotoImage(img2)
    img_lable1 = Label(root, image=img2)
    img_lable1.image = img2
    img_lable1.place(x=700, y=260)

def cauchy_solve():
    x = 0.2
    y = 0.25
    delta_x=0.1
    x_values = [x]
    y_values = [y]
    while x <= 1.2:
        old_x = x
        x = x + delta_x
        y = y + delta_x * (0.133 * (old_x ** 2 + math.sin(2 * old_x) + 0.872 * y))
        x_values.append(x)
        y_values.append(y)
        rx_val=['{:.4f}'.format(n) for n in x_values]
        ry_val = ['{:.4f}'.format(n) for n in y_values]

    result_label5 = Label(root, text='Усовершенствованный метод ломанных', font='Courier 13').place(x=30, y=490)
    result_label6 = Label(root, text='По х: ' + ', '.join(rx_val), font='Courier 10').place(x=30, y=520)
    result_label7 = Label(root, text='По y: ' +', '.join(ry_val), font='Courier 10').place(x=30, y=550)

    img2 = Image.open('задание3.png')
    img2 = ImageTk.PhotoImage(img2)
    img_lable1 = Label(root, image=img2)
    img_lable1.image = img2
    img_lable1.place(x=700, y=450)

btn_calculate1 = Button(root, text="Задание 1", bg='HotPink4',command=a).place(x=185, y=50)
btn_calculate2 = Button(root, text="Задание 2", bg='HotPink4',command=calculate_integral).place(x=185, y=250)
btn_calculate3 = Button(root, text="Задание 3", bg='HotPink4',command=cauchy_solve).place(x=185,y=450)

# График заданной функции 1 задание
x = linspace(-4, 5, 50)
y = f(x)
plt.figure()
plt.plot(x, y)
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.title('График функции у = 2x^3 - 3x^2 - 12x - 5')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()

root.mainloop()