import numpy as np
import matplotlib.pyplot as plt


def percentage(length, fraction):
    return int(length * fraction / 100)


class NoLineal:
    def __init__(self, x, y, p, alpha, epoch):
        self.x = x
        self.y = y
        self.p = p
        self.alpha = alpha
        self.epoch = epoch

        self.xTrain = self.x[:percentage(len(x), 70)]
        self.xValidation = self.x[percentage(
            len(x), 70):percentage(len(x), 90)]
        self.xTest = self.x[percentage(len(x), 90):]

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
        return err

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
                    (-x[i] ** (j + 1))

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
        # errTrain = self.error(w, b, self.x)
        errorListTrain = [errTrain]
        errorListValidation = []

        for i in range(self.epoch):
            db, dw = self.derivative(w, b, self.xTrain)
            # db, dw = self.derivative(w, b, self.x)

            b, w = self.update(b, db, w, dw)

            errTrain = self.error(w, b, self.xTrain)
            # errTrain = self.error(w, b, self.x)
            errValidation = self.error(w, b, self.xValidation)

            errorListTrain.append(errTrain)
            errorListValidation.append(errValidation)

        plt.plot(errorListTrain)
        plt.plot(errorListValidation)
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

# plt.plot(x, y, '*')
# plt.show()

noLineal = NoLineal(tempX, tempY, 2, 0.001, 200)
noLineal.train()

noLineal1 = NoLineal(tempX, tempY, 2, 0.2, 200)
noLineal1.train()

noLineal2 = NoLineal(tempX, tempY, 2, 0.5, 200)
noLineal2.train()
