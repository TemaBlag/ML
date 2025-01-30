import numpy as np
import matplotlib.pyplot as plt

x_train = np.array([[10, 50], [20, 30], [25, 30], [20, 60], [15, 70], [40, 40], [30, 45], [20, 45], [40, 30], [7, 35]])
x_train = np.array(list(map(lambda x: np.append(x, 1), x_train)))
y_train = np.array([-1, 1, 1, -1, -1, 1, 1, -1, 1, -1])
n_train = 10
sum_xy = np.sum([x * y for x, y in zip(x_train, y_train)], axis=0)
sum_xx = np.sum([np.outer(x ,x.T) for x in x_train], axis=0)
w = np.dot(sum_xy, np.linalg.inv(sum_xx))

line_x = list(range(max(x_train[:, 0])))
line_y = [-w[0]*x/w[1] - w[2]/w[1] for x in line_x]

x_0 = x_train[y_train == 1]
x_1 = x_train[y_train == -1]

plt.scatter(x_0[:, 0], x_0[:, 1], color='red')
plt.scatter(x_1[:, 0], x_1[:, 1], color='blue')
plt.plot(line_x, line_y, color='green')

plt.xlim([0, 45])
plt.ylim([0, 75])
plt.ylabel("длина")
plt.xlabel("ширина")
plt.grid(True)
plt.show()

print(w)