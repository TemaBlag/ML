import numpy as np
import matplotlib.pyplot as plt

x_train = np.array([[10, 50], [20, 30], [25, 30], [20, 60], [15, 70], [40, 40], [30, 45], [20, 45], [40, 30], [7, 35]])
y_train = np.array([-1, 1, 1, -1, -1, 1, 1, -1, 1, -1])

w = np.array([0, -1])
n_train = 10
n = 50
coefficient = 0.1
coefficient_editing = 0.1
func = lambda x: w @ x

last_error_index = -1
for k in range(n):
    for i in range(n_train):
        x = np.array(x_train[i]).T
        y = y_train[i]
        if func(x) * y < 0:
            w = np.array([w[0] + coefficient * y, -1])
            last_error_index = i

    Q = sum([1 for l in range(n_train) if func(x_train[l]) * y_train[l] < 0])
    if not Q:
        break
if last_error_index != -1:
    w[0] += coefficient_editing * y_train[last_error_index]
print(w)

line_x = list(range(max(x_train[:, 0])))    # формирование графика разделяющей линии
line_y = [w[0]*x for x in line_x]

x_0 = x_train[y_train == 1]                 # формирование точек для 1-го
x_1 = x_train[y_train == -1]                # и 2-го классов

plt.scatter(x_0[:, 0], x_0[:, 1], color='red')
plt.scatter(x_1[:, 0], x_1[:, 1], color='blue')
plt.plot(line_x, line_y, color='green')

plt.xlim([0, 45])
plt.ylim([0, 75])
plt.ylabel("длина")
plt.xlabel("ширина")
plt.grid(True)
plt.show()

