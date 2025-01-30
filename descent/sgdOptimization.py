# optimization - Nesterov momentum
import numpy as np
import matplotlib.pyplot as plt
import math
import random

x_train = np.array([[10, 50], [20, 30], [25, 30], [20, 60], [15, 70], [40, 40], [30, 45], [20, 45], [40, 30], [7, 35]])
x_train = np.array(list(map(lambda x: np.append(x, 1), x_train)))
y_train = np.array([-1, 1, 1, -1, -1, 1, 1, -1, 1, -1])

# initialization
n_train = 10
nt = 0.0005
lm = 0.01
n = 500
w = [0.0, 0.0, 0.0]
moment_coef = 0.9


def func_lose(w, x, y):
    return 2 / (1 + math.exp(np.dot(w, x) * y))


def dfunc_lose(w, x, y):
    return - 2 * np.dot(x, y) * math.exp(np.dot(w, x) * y) * (1 + math.exp(np.dot(w, x) * y)) ** (-2)


Q = np.sum([func_lose(w, x, y) for x, y in zip(x_train, y_train)])
Q_plot = [Q]


def stohasticGradientDescent_NAG(w, x_train, y_train, n_train, lm, nt):
    global Q
    vt = np.array([0] * len(w))
    while Q > 0.1:
        k = random.randint(0, n_train - 1)
        ek = func_lose(w, x_train[k], y_train[k])
        vt = vt * moment_coef - nt * dfunc_lose(w - vt * moment_coef, x_train[k], y_train[k])
        w = w + vt
        Q = ek * lm + (1 - lm) * Q
        Q_plot.append(Q)
    return w


w = stohasticGradientDescent_NAG(w, x_train, y_train, n_train, lm, nt)
print(w)
print(Q_plot)

line_x = list(range(max(x_train[:, 0])))
line_y = [-x * w[0] / w[1] - w[2] / w[1] for x in line_x]

x_1 = x_train[y_train == 1]
x_0 = x_train[y_train == -1]

plt.scatter(x_0[:, 0], x_0[:, 1], color='red')
plt.scatter(x_1[:, 0], x_1[:, 1], color='blue')

plt.plot(line_x, line_y, color='green')

plt.xlim([0, 45])
plt.ylim([0, 75])
plt.grid(True)
plt.xlabel('длина')
plt.ylabel('ширина')
plt.show()