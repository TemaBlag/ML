import numpy as np
import math
import matplotlib.pyplot as plt
import random

x_train = [[10, 50], [20, 30], [25, 30], [20, 60], [15, 70], [40, 40], [30, 45], [20, 45], [40, 30], [7, 35]]
x_train = np.array([x + [10*x[0], 10*x[1], 5*(x[0]+x[1])] for x in x_train])
y_train = np.array([-1, 1, 1, -1, -1, 1, 1, -1, 1, -1])

def func_lose(w, x, y):
    express = np.dot(w, x) * y
    return 2 / (1 + math.exp(express))


def dfunc_lose(w, x, y):
    express = np.dot(w, x) * y
    L1 = 0.01
    return - 2 * np.dot(x, y) * math.exp(express) / ((1 + math.exp(express)) ** 2) + L1 * np.sign(w)


w = np.array([0, 0, 0, 0, 0])
n_train = 10
nt = 0.00001
lm = 0.01
n = 500
Q = np.mean([func_lose(w, x, y) for x, y in zip(x_train, y_train)])
Q_plot = [Q]

def stohasticGradientDescent_L1_Regularization(w, x_train, y_train, n, n_train, lm, nt):
    global Q
    while Q > 0.1:
        k = random.randint(0, n_train - 1)
        ek = func_lose(w, x_train[k], y_train[k])
        w = w - nt * dfunc_lose(w, x_train[k], y_train[k])
        Q = ek * lm + (1 - lm) * Q
        Q_plot.append(Q)
    return w



w = stohasticGradientDescent_L1_Regularization(w, x_train, y_train, n, n_train, lm, nt)

Q = np.mean([func_lose(x, w, y) for x, y in zip(x_train, y_train)]) # истинное значение эмпирического риска после обучения
print(w)
print(Q)

plt.plot(Q_plot)
plt.grid(True)
plt.show()

