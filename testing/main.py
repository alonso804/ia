import numpy as np
from numpy.random import default_rng
# from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import random

x = np.linspace(0, 1, num=100)
y = [np.sin(i*2*3.14) + np.random.normal(0, 0.1) for i in x]
plt.plot(x, y, '*')

xy = []
for i in range(len(x)):
    xy.append((x[i], y[i]))

np.random.shuffle(xy)

tempX = []
tempY = []
for i in xy:
    tempX.append(i[0])
    tempY.append(i[1])

x = tempX
y = tempY

y_train, y_validate, y_test = y[:70], y[70:90], y[90:]
x_train, x_validate, x_test = x[:70], x[70:90], x[90:]


def h(x, w, b):
    return np.matmul(w, np.transpose(x)) + b


def Error(y, x, b, w):
    m = len(x)
    l = 0
    for i in range(m):
        l = l + (y[i]-h(x, w, b))**2
    l = l/(2*m)
    return l


def derivada(y, x, b, w):
    # implementar código
    db = 0
    dw = 0
    for i in range(m):
        for j in range(k):
            dw = dw + (y[i]-h(x[i], w, b))*(-1*x[i][j])
        db = db + (y[i]-h(x[i], w, b))*(-1)
    dw = dw/m
    db = db/m
    return db, dw


def update(w, b, alfa, dw, db):
    w = w - (alfa*dw)
    b = b - (alfa*db)
    return w, b


def train(x, y, alfa, umbral, k):
    w = np.array(np.random.rand() for j in range(4))
    b = np.random.rand()
    error_t = Error(y_train, x_train, b, w)
    error_v = Error(y_validate, x_validate, b, w)
    t_error = []
    v_error = []
    for i in range(umbral):
        db, dw = derivada(y_train, x, b, w)
        w, b = update(w, b, alfa, dw, db)
        error_t = Error(y_train, x_train, b, w)
        error_v = Error(y_validate, x_validate, b, w)
        t_error.append(error_t)
        v_error.append(error_v)
        print("t:", error_t, " v:", error_v)


    # plt.plot(error_t)
    # plt.plot(error_v)
k = 2
x = default_rng(42).random((100, k))
y = np.array([j + np.random.normal(0, 0.5) for j in range(100)])


m = len(x)

# fig = plt.figure()
# ax = plt.axes(projection='3d')
# ax.scatter3D(x[:, 0], x[:, 1], y)
# plt.show()

train(x, y, 0.0001, 5000, k)
