import numpy as np
import matplotlib.pyplot as plt


def percentage(length, fraction):
    return int(length * fraction / 100)


class NoLineal:
    def __init__(self, x, y, p, alpha, epoch):
        self.x = x
        self.y = y
        self.p = p
        self.m = len(x)
        self.alpha = alpha
        self.epoch = epoch
        # np.random.shuffle(xy)

    def hypothesis(self, xi, w, b):
        h = 0
        for i in range(self.p):
            h += w[i] * (xi ** (i + 1))

        h += b

        return h

    def error(self, w, b):
        err = 0

        for i in range(self.m):
            err += (y[i] - self.hypothesis(self.x[i], w, b)) ** 2

        err /= (2 * self.m)
        return err

    def derivative(self, w, b):
        db = 0

        for i in range(self.m):
            db += (self.y[i] - self.hypothesis(x[i], w, b)) * (-1)

        db /= self.m

        dw = [0] * len(w)
        for j in range(len(w)):
            for i in range(self.m):
                dw[j] += (self.y[i] - self.hypothesis(x[i], w, b)) * \
                    (-self.x[i] ** (j + 1))

            dw[j] /= self.m

        return db, dw

    def update(self, b, db, w, dw):
        b -= self.alpha * db

        for j in range(len(w)):
            w[j] -= self.alpha * dw[j]

        return b, w

    def train(self):
        w = [np.random.rand() for i in range(self.p)]
        b = np.random.rand()

        err = self.error(w, b)
        errorList = [err]

        for i in range(self.epoch):
            db, dw = self.derivative(w, b)
            b, w = self.update(b, db, w, dw)
            err = self.error(w, b)
            errorList.append(err)

        plt.plot(errorList, '*')
        plt.show()


x = np.linspace(0, 1, num=100)
y = [np.sin(i * 2 * 3.14) + np.random.normal(0, 0.1) for i in x]

# plt.plot(x, y, '*')
# plt.show()

noLineal = NoLineal(x, y, 2, 0.1, 200)
noLineal.train()
