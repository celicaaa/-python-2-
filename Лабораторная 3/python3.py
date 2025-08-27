from tkinter import *
import os
import scipy
from scipy.optimize import fsolve

root = Tk()
root.title('Lab3')
root.geometry('800x500')
root.configure(background='rosybrown')
img = PhotoImage(file='фото.png')
im =Label(image=img)
im.place(x=100, y=300)



# Гаусс
def gauss_solution(A, B):
    n = len(A)
    for k in range(n):
        for i in range(k + 1, n):
            coef = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] -= coef * A[k][j]
            B[i] -= coef * B[k]
    X = [0] * n
    for k in range(n - 1, -1, -1):
        X[k] = (B[k] - sum(A[k][j] * X[j] for j in range(k + 1, n))) / A[k][k]
    return X


# Гаус-Жордан
def gauss_jordan_solution(A, B):
    n = len(A)
    for k in range(n):
        for i in range(n):
            if i != k:
                coef = A[i][k] / A[k][k]
                for j in range(k, n):
                    A[i][j] -= coef * A[k][j]
                B[i] -= coef * B[k]
                A[i][k] = 0
    X = [B[i] / A[i][i] for i in range(n)]
    return X


A = [[5.4, -6.2, -0.5],
     [3.4, 2.3, 0.8],
     [2.4, -1.1, 3.8]]
B = [0.52, -0.8, 1.8]


def b1():
    X_gauss = gauss_solution(A, B)
    X_gauss_rounded = [round(x, 6) for x in X_gauss]
    result1 = "\n".join(str(x) for x in X_gauss_rounded)
    lab1 = Label(text=result1)
    lab1.place(x=25,y=50)
    f = open('lab3.txt', 'a+')
    f.write('Метод Гаусса: \n')
    f.write(result1 + '\n' + '\n')
    f.close()


def b23():
    X_gauss_jordan = gauss_jordan_solution(A, B)
    X_gauss_jordan_rounded = [round(x, 6) for x in X_gauss_jordan]
    result2 = "\n".join(str(x) for x in X_gauss_jordan_rounded)
    lab2 = Label(text=result2)
    lab2.place(x=130,y=50)
    f = open('lab3.txt', 'a+')
    f.write('Метод Гаусса-Жордана: \n')
    f.write(result2 + '\n' + '\n')
    f.close()


def equationss(vars):
    x, y, z = vars
    eq1 = 5.4 * x - 6.2 * y - 0.5 * z + 0.52
    eq2 = 3.4 * x + 2.3 * y + 0.8 * z - 0.8
    eq3 = 2.4 * x - 1.1 * y + 3.8 * z + 1.8

    return eq1, eq2, eq3


def scipy():
    x, y, z = fsolve(equationss, (0, 0, 0))
    x = round(x, 6)
    y = round(y, 6)
    z = round(z, 6)
    lab3 = Label(text=(str(-x) + '\n' + str(-y) + '\n' + str(-z)))
    lab3.place(x=275,y=50)
    f = open('lab3.txt', 'a+')
    f.write('Scipy: \n')
    f.write((str(-x) + '\n' + str(-y) + '\n' + str(-z)))
    f.close()


def file1():
    os.startfile('lab3.txt')


def file2():
    os.startfile('excel3.xlsx')

def file3():
    os.startfile('matlab3.m')


b22 = Button(text='Метод Гаусса', command=b1 )
b22.place(x=10, y=10)

b33 = Button(text='Метод Гаусса-Жордана', command=b23)
b33.place(x=100, y=10)

b333 = Button(text='Scipy', command=scipy)
b333.place(x=280, y=10)

b44 = Button(text='Текст', command=file1)
b44.place(x=450,y=10)

b55 = Button(text='Excel', command=file2)
b55.place(x=400,y=10)

b55 = Button(text='Matlab', command=file3)
b55.place(x=500,y=10)

root.mainloop()
