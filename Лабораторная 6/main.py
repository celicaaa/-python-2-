from numpy import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import Frame
from PIL import Image, ImageTk

def f(x, y):
    return x*exp(-(x**2)) - 2*x*y

def real(x):
    return exp(-(x**2))*(0.5*x**2+1)

def f1(y1, y2):
    return 2*y1+y2

def f2(y1, y2):
    return 3*y1+4*y2

def real_y1(x):
    return exp(x)+exp(5*x)

def real_y2(x):
    return -exp(x)+3*exp(5*x)

def euler_method(f, x0, y0, h, xn):
    n = int((xn - x0) / h)
    x = linspace(x0, xn, n + 1)
    y = zeros(n + 1)
    y[0] = y0
    for i in range(n):
        y[i + 1] = y[i] + h * f(x[i], y[i])
    return x, y

def runge_kutta(f, x0, y0, h, xn):
    n = int((xn - x0) / h)
    x = linspace(x0, xn, n + 1)
    y = zeros(n + 1)
    y[0] = y0
    for i in range(n):
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + h / 2, y[i] + k1 / 2)
        k3 = h * f(x[i] + h / 2, y[i] + k2 / 2)
        k4 = h * f(x[i] + h, y[i] + k3)
        y[i + 1] = y[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return x, y

def euler_system(f1, f2, x0, y10, y20, h, xn):
    n = int((xn - x0) / h)
    x = linspace(x0, xn, n + 1)
    y1 = zeros(n + 1)
    y2 = zeros(n + 1)
    y1[0] = y10
    y2[0] = y20
    for i in range(n):
        y1[i + 1] = y1[i] + h * f1(y1[i], y2[i])
        y2[i + 1] = y2[i] + h * f2(y1[i], y2[i])
    return x, y1, y2

def runge_kutta_system(f1, f2, x0, y10, y20, h, xn):
    n = int((xn - x0) / h)
    x = linspace(x0, xn, n + 1)
    y1 = zeros(n + 1)
    y2 = zeros(n + 1)
    y1[0] = y10
    y2[0] = y20
    for i in range(n):
        k1_y1 = h * f1(y1[i], y2[i])
        k1_y2 = h * f2(y1[i], y2[i])
        
        k2_y1 = h * f1(y1[i] + 0.5 * k1_y1, y2[i] + 0.5 * k1_y2)
        k2_y2 = h * f2(y1[i] + 0.5 * k1_y1, y2[i] + 0.5 * k1_y2)
        
        k3_y1 = h * f1(y1[i] + 0.5 * k2_y1, y2[i] + 0.5 * k2_y2)
        k3_y2 = h * f2(y1[i] + 0.5 * k2_y1, y2[i] + 0.5 * k2_y2)
        
        k4_y1 = h * f1(y1[i] + k3_y1, y2[i] + k3_y2)
        k4_y2 = h * f2(y1[i] + k3_y1, y2[i] + k3_y2)
        
        y1[i + 1] = y1[i] + (k1_y1 + 2 * k2_y1 + 2 * k3_y1 + k4_y1) / 6
        y2[i + 1] = y2[i] + (k1_y2 + 2 * k2_y2 + 2 * k3_y2 + k4_y2) / 6
    return x, y1, y2

window = tk.Tk()
window.geometry('1500x800')
window.config(bg='light steel blue')
window.title('Л/р №6 Астраханкина')

frame = Frame(window)
frame.pack(fill='both', expand=True)
frame.place(x=0, y=0)

fig = plt.Figure(figsize=(11, 5), dpi=75)

image1 = Image.open("task1.png")
photo1 = ImageTk.PhotoImage(image1)
label1 = tk.Label(window, image=photo1)
label1.place(x=850, y=15)

image2 = Image.open("task2.png")
photo2 = ImageTk.PhotoImage(image2)
label2 = tk.Label(window, image=photo2)
label2.place(x=850, y=150)

image3 = Image.open("usl1.jpg")
photo3 = ImageTk.PhotoImage(image3)
label3 = tk.Label(window, image=photo3)
label3.place(x=850, y=90)

image4 = Image.open("usl2.jpg")
photo4 = ImageTk.PhotoImage(image4)
label4 = tk.Label(window, image=photo4)
label4.place(x=850, y=335)

x0 = 0
y0 = 1
h = 0.1
xn = 1
y10 = 2
y20 = 2

plot1 = fig.add_subplot(121)
x_euler, y_euler = euler_method(f, x0, y0, h, xn)
x_rk, y_rk = runge_kutta(f, x0, y0, h, xn)
x_exact = linspace(x0, xn, 11)
y_exact = real(x_exact)
plot1.plot(x_euler, y_euler, 'o-', label='Метод Эйлера')
plot1.plot(x_rk, y_rk, 's-', label='Метод Рунге-Кутта')
plot1.plot(x_exact, y_exact, '-', label='Точное решение')
plot1.set_xlabel('x')
plot1.set_ylabel('y')
plot1.legend()
plot1.set_title('ОДУ первого порядка')
plot1.grid(True)

plot2 = fig.add_subplot(122)
x_euler_sys, y1_euler, y2_euler = euler_system(f1, f2, x0, y10, y20, h, xn)
x_rk4_sys, y1_rk4, y2_rk4 = runge_kutta_system(f1, f2, x0, y10, y20, h, xn)
y1_exact_sys = real_y1(x_exact)
y2_exact_sys = real_y2(x_exact)
plot2.plot(x_euler_sys, y1_euler, 'o-', label='Метод Эйлера y1')
plot2.plot(x_rk4_sys, y1_rk4, 's-', label='Метод Рунге-Кутта y1')
plot2.plot(x_exact, y1_exact_sys, '-', label='Точное решение y1')
plot2.plot(x_euler_sys, y2_euler, 'o--', label='Метод Эйлера y2')
plot2.plot(x_rk4_sys, y2_rk4, 's--', label='Метод Рунге-Кутта y2')
plot2.plot(x_exact, y2_exact_sys, '--', label='Точное решение y2')
plot2.set_xlabel('x')
plot2.set_ylabel('y')
plot2.legend()
plot2.set_title('Система ОДУ первого порядка')
plot2.grid(True)

canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.draw()
canvas.get_tk_widget().pack()

textr1 = tk.Label(window, text='Точное решение:',background='lavender').place(x=25, y=500)
texteuler = tk.Label(window, text='Метод Эйлера:',background='lavender').place(x=25, y=550)
textrenkut = tk.Label(window, text='Метод Рунге-Кутта:',background='lavender').place(x=25, y=600)

y_real = []
for i in y_exact:
    y_real.append(round(i, 4))

y_euler_ins = []
for i in y_euler:
    y_euler_ins.append(round(i, 4))

y_rk_ins = []
for i in y_rk:
    y_rk_ins.append(round(i, 4))

r1ans = tk.Entry(window)
r1ans.place(x=200, y=502, width=500)
r1ans.insert(0, f'{y_real}')
reuler = tk.Entry(window)
reuler.place(x=200, y=552, width=500)
reuler.insert(0, f'{y_euler_ins}')
rrenkut = tk.Entry(window)
rrenkut.place(x=200, y=602, width=500)
rrenkut.insert(0, f'{y_rk_ins}')

textrsys = tk.Label(window, text='Точное решение Y1:', background='lavender').place(x=800, y=450)
textrsys = tk.Label(window, text='Точное решение Y2:', background='lavender').place(x=800, y=500)
texteulersys = tk.Label(window, text='Метод Эйлера Y1:', background='lavender').place(x=800, y=550)
texteulersys = tk.Label(window, text='Метод Эйлера Y2:',background='lavender').place(x=800, y=600)
textrenkutsys = tk.Label(window, text='Метод Рунге-Кутта Y1:', background='lavender').place(x=800, y=650)
textrenkutsys = tk.Label(window, text='Метод Рунге-Кутта Y2:',  background='lavender').place(x=800, y=700)

y1_exact_sys_ans = []
for i in y1_exact_sys:
    y1_exact_sys_ans.append(round(i, 4))

y2_exact_sys_ans = []
for i in y2_exact_sys:
    y2_exact_sys_ans.append(round(i, 4))

y1_euler_ans = []
for i in y1_euler:
    y1_euler_ans.append(round(i, 4))

y2_euler_ans = []
for i in y2_euler:
    y2_euler_ans.append(round(i, 4))

y1_rk4_ans = []
for i in y1_rk4:
    y1_rk4_ans.append(round(i, 4))

y2_rk4_ans = []
for i in y2_rk4:
    y2_rk4_ans.append(round(i, 4))

rsysansy1 = tk.Entry(window)
rsysansy1.place(x=950, y=452, width=500)
rsysansy1.insert(0, f'{y1_exact_sys_ans}')
rsysansy2 = tk.Entry(window)
rsysansy2.place(x=950, y=502, width=500)
rsysansy2.insert(0, f'{y2_exact_sys_ans}')
eulersysansy1 = tk.Entry(window)
eulersysansy1.place(x=950, y=552, width=500)
eulersysansy1.insert(0, f'{y1_euler_ans}')
eulersysansy2 = tk.Entry(window)
eulersysansy2.place(x=950, y=602, width=500)
eulersysansy2.insert(0, f'{y2_euler_ans}')
renkutsysansy1 = tk.Entry(window)
renkutsysansy1.place(x=950, y=652, width=500)
renkutsysansy1.insert(0, f'{y1_rk4_ans}')
renkutsysansy2 = tk.Entry(window)
renkutsysansy2.place(x=950, y=702, width=500)
renkutsysansy2.insert(0, f'{y2_rk4_ans}')

window.mainloop()