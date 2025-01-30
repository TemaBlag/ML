import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 100, 0.5)
func = lambda x: x ** 4 + x ** 3 + x ** 2 + x + 1
y = np.array(list(map(func, x)))
x_train, y_train = x[::2], y[::2]
N, L = 16, 0.85
IL = np.array([[L if i == j else 0 for j in range(N)] for i in range(N)])
IL[0][0] = 0

X = np.array([[i ** j for j in range(N)] for i in x])
X_train = X[::2]
A = np.linalg.inv(IL + np.dot(X_train.T, X_train))
w = y_train @ X_train @ A
print(w)

yy = [np.dot(w, val) for val in X]
plt.plot(x, yy)
plt.plot(x, y)
plt.grid(True)
plt.show()


