import numpy as np


class SVM:
    def __init__(self, x, y, alpha, epoch):
        self.x = x
        self.y = y
        self.alpha = alpha
        self.epoch = epoch

    def derivative(self, lamb, x):
        n = len(self.y)
        dw = [0] * k
        db = 0
        for i in range(n):
            for j in range(k):
                dw += lamb*(self.y[i])*x[j]

    def train(self):
        w = [np.random.rand() for i in range(len(self.x))]
        b = np.random.rand()

        for i in range(self.epoch):
            p = np.random(0, len(self.x))
            x = self.x[p]
            y = self.y[p]

            for i in range(len(w)):
                if y[i] * (np.dot(w, x) + b) >= 1:
                    w[i] -= self.alpha * w[i]
                else:
                    w[i] -= self.alpha * (w[i] - y[i] * x[i])
                    b -= self.alpha * (-self.y[i])
