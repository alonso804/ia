import numpy as np
import matplotlib.pyplot as plt


def percentage(length, fraction):
    return int(length * fraction / 100)


class NoLineal:
    def __init__(self, x, y, p, alpha, epoch, lambd, degree):
        self.x = x
        self.y = y
        self.p = p
        self.alpha = alpha
        self.epoch = epoch
        self.lambd = lambd
        self.degree = degree

        self.xTrain = self.x[:percentage(len(x), 70)]
        self.xValidation = self.x[percentage(
            len(x), 70):percentage(len(x), 90)]
        self.xTest = self.x[percentage(len(x), 90):]

    def regularization(self, w, m):
        reg = 0

        for i in range(self.p):
            reg += w[i] ** self.degree

        reg *= self.lambd
        reg /= m

        return reg

    def hypothesis(self, xi, w, b):
        h = 0
        for i in range(self.p):
            h += w[i] * (xi ** (i + 1))

        h += b

        return h

    def error(self, w, b, x):
        m = len(x)
        err = 0

        for i in range(m):
            err += (y[i] - self.hypothesis(x[i], w, b)) ** 2

        err /= (2 * m)

        reg = self.regularization(w, m)
        return err + reg

    def derivative(self, w, b, x):
        m = len(x)
        db = 0

        for i in range(m):
            db += (self.y[i] - self.hypothesis(x[i], w, b)) * (-1)

        db /= m

        dw = [0] * len(w)
        for j in range(len(w)):
            for i in range(m):
                dw[j] += (self.y[i] - self.hypothesis(x[i], w, b)) * \
                    -x[i] ** (j + 1)

            dw[j] /= m

        return db, dw

    def update(self, b, db, w, dw):
        b -= self.alpha * db

        for j in range(len(w)):
            w[j] -= self.alpha * dw[j]

        return b, w

    def train(self):
        w = [np.random.rand() for i in range(self.p)]
        b = np.random.rand()

        errTrain = self.error(w, b, self.xTrain)
        errTest = self.error(w, b, self.xTest)
        errorListTrain = [errTrain]
        errorListTest = [errTest]
        errorListValidation = []

        for i in range(self.epoch):
            db, dw = self.derivative(w, b, self.xTrain)

            b, w = self.update(b, db, w, dw)

            errTrain = self.error(w, b, self.xTrain)
            errTest = self.error(w, b, self.xTest)
            errValidation = self.error(w, b, self.xValidation)

            errorListTrain.append(errTrain)
            errorListTest.append(errTest)
            errorListValidation.append(errValidation)

        """
        print(w, b)
        ys = [self.hypothesis(xi, w, b) for xi in self.x]
        print(self.x)
        print(ys)
        print()
        """
        ys = [self.hypothesis(xi, w, b) for xi in self.xTrain]
        plt.plot(self.x, self.y, '*')
        plt.plot(self.xTrain, ys, '*')

        # plt.plot(errorListTrain)
        # plt.plot(errorListTest)
        # plt.plot(errorListValidation)
        plt.show()


x = np.linspace(0, 1, num=100)
y = [np.sin(i * 2 * 3.14) + np.random.normal(0, 0.1) for i in x]

tempX = []
tempY = []

xy = []

for i in range(len(x)):
    xy.append((x[i], y[i]))

np.random.shuffle(xy)

for i in range(len(xy)):
    tempX.append(xy[i][0])
    tempY.append(xy[i][1])

#noLineal = NoLineal(tempX, tempY, 2, 0.025, 200, 1000)
#                  (x, y, p, alpha, epoch, lambd, degree)
noLineal = NoLineal(tempX, tempY, 5, 0.0024, 50000, 8, 2)
# noLineal = NoLineal(tempX, tempY, 10, 0.001, 3500, 100, 2)
# noLineal.train()
# p = 5
# alpha = 0.0024
# epoch = 50000
# lambda = 8

noLineal1 = NoLineal(tempX, tempY, 5, 0.025, 200, 100, 2)
# noLineal1.train()

noLineal2 = NoLineal(tempX, tempY, 2, 0.025, 200, 100, 2)
# noLineal2.train()
