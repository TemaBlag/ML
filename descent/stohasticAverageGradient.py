import numpy as np
import matplotlib.pyplot as plt
import random
import math
from scipy.special import expit


x_train = np.array([[10, 50], [20, 30], [25, 30], [20, 60], [15, 70], [40, 40], [30, 45], [20, 45], [40, 30], [7, 35]])
x_train = np.array(list(map(lambda x: np.append(x, 1), x_train)))
y_train = np.array([-1, 1, 1, -1, -1, 1, 1, -1, 1, -1])

# initialization
n_train = 10
nt = 0.01
lm = 0.01
n = 100
w = [0.1, 0.1, 0.1]
G, Q_plot = [], []


def func_lose(w, x, y):
    exp_term = np.dot(w, x) * y
    return 2 / (1 + math.exp(exp_term))


def dfunc_lose(w, x, y):
    exp_term = np.dot(w, x) * y
    return - 2 * x * y * math.exp(exp_term) * (1 + math.exp(exp_term)) ** (-2)

def all_gradients(func, x_train, y_train):
    global G
    for x, y in zip(x_train, y_train):
        G.append(func(w, x, y))


def stohasticAverageGradient(w, x_train, y_train, n, n_train, lm, nt):
    global Q
    global G
    all_gradients(dfunc_lose, x_train, y_train)
    g_mean = np.mean(G, axis=0)
    Q = np.sum([func_lose(w, x, y) for x, y in zip(x_train, y_train)])
    Q_plot.append(Q)
    while Q > 0.5:
        k = random.randint(0, n_train - 1)
        ek = func_lose(w, x_train[k], y_train[k])
        new_g_k = dfunc_lose(w, x_train[k], y_train[k])
        g_k, G[k] = G[k], new_g_k
        g_mean = g_mean - (g_k - new_g_k) / n_train
        w = w - nt * g_mean
        Q = ek * lm + (1 - lm) * Q
        Q_plot.append(Q)
    return w


w = stohasticAverageGradient(w, x_train, y_train, n, n_train, lm, nt)
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
plt.xlabel('ширина')
plt.show()