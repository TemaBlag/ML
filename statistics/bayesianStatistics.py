"""
const = 8
nums = [1, 2, 3, 4, 5, 6]
res = 0
for x in range(1, 7):
    for y in range(1, 7):
        c = x + y if x + y < 8 else 7
        res += nums[c-2]
print(res)
"""
"""
биномиальное распределение
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, beta

# Задаем параметры биномиального распределения
n = 7  # Количество испытаний
p = 0.2  # Вероятность успеха в каждом испытании

# Создаем массив значений количества успешных исходов
k_values = np.arange(0, n+1)

# Вычисляем вероятности для каждого значения успешных исходов
probabilities = binom.pmf(k_values, n, p)

# Строим график биномиального распределения
plt.bar(k_values, probabilities)
plt.xlabel('Количество успешных исходов')
plt.ylabel('Вероятность')
plt.title('Биномиальное распределение (n={}, p={})'.format(n, p))
plt.show()
k = 1
print(1 - binom.cdf(1, 25, 0.1))
print(1 - binom.cdf(1, n, p))
"""
"""
бета-распределение
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta
from scipy.integrate import quad

# Задаем параметры бета-распределения
alpha = 6
beta1 = 1

# Создаем массив значений для оси x
x = np.linspace(0, 1, 100)

# Вычисляем значения плотности вероятности (PDF) для каждого значения x
pdf = beta.pdf(x, alpha + 55, beta1 + 55)

# Строим график бета-распределения
plt.plot(x, pdf)
plt.xlabel('Значение')
plt.ylabel('Плотность вероятности')
plt.title('Бета-распределение (alpha={}, beta={})'.format(alpha, beta))
plt.show()

def integrand(x):
    return beta.pdf(x, alpha + 55 + 25, beta1 + 55)

result, error = quad(integrand, 0.4, 0.6)
print("Значение интеграла: ", result)
"""
"""
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from scipy.integrate import quad

x = [2.5, 3, 3.5, 4, 2]
mean = np.mean(x)
std_dev = np.std(x)
pdf = norm.pdf(sorted(x), loc=mean, scale=std_dev)
plt.plot(sorted(x), pdf, 'b-', linewidth=2)
plt.xlabel('Значение')
plt.ylabel('Плотность вероятности')
plt.title('Нормальное распределение')
plt.grid(True)
plt.show()
def integrand(x):
    return norm.pdf(x, loc=mean, scale=std_dev)
result, error = quad(integrand, -10, 0)
print("Значение интеграла: ", result)
print(mean)
print(std_dev)

Кумулятивная функция
import numpy as np
from scipy.stats import norm
from scipy.stats import beta
import matplotlib.pyplot as plt
x = [7.8, 9.4, 10, 7.9, 7, 7, 7.1, 8.9, 7.4]  # диапазон значений
mean = np.mean(x)
std_dev = np.std(x)
cdf = norm.cdf(sorted(x), loc=mean, scale=std_dev)
plt.plot(sorted(x), cdf, 'b-', linewidth=2)
plt.xlabel('Значение')
plt.ylabel('CDF')
plt.title('Кумулятивная функция распределения (CDF)')
plt.grid(True)
plt.show()
print(beta.pdf(sorted(x), loc=mean, scale=std_dev))
"""
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta
alpha = 6
beta1 = 1
x = np.linspace(0.005, 0.01, 100)
pdf = beta.cdf(x, 300, 39700)
plt.plot(x, pdf)
plt.xlabel('Значение')
plt.ylabel('Плотность вероятности')
plt.title('Бета-распределение (alpha={}, beta={})'.format(alpha, beta))
plt.show()
print(beta.cdf(1, 300, 39700) - beta.cdf(0.0085, 300, 39700))
"""
"""
квантильной функции
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
mean = 0  # среднее значение
std_dev = 1  # стандартное отклонение
probabilities = np.linspace(0.01, 0.99, 100)  # Задаем массив вероятностей
quantiles = norm.ppf(probabilities, loc=mean, scale=std_dev)  # Вычисляем квантили для каждой вероятности
plt.plot(probabilities, quantiles, 'b-', linewidth=2)
plt.xlabel('Вероятность')
plt.ylabel('Квантиль')
plt.title('Квантильная функция нормального распределения (среднее={}, стандартное отклонение={})'.format(mean, std_dev))
plt.grid(True)
plt.show()
"""
"""
from scipy.stats import norm
mean = 3
std_dev = 0
probability = 0.975
quantile = norm.ppf(probability, loc=mean, scale=std_dev)
print("Квантиль для вероятности", probability, ":", quantile)
"""
"""
from scipy.stats import beta
a = 9  # параметр a бета-распределения
b = 3  # параметр b бета-распределения
dist = beta(a, b)  # создание объекта распределения бета
lower_bound = dist.ppf(0.025)
upper_bound = dist.ppf(0.975)
print("Нижняя граница доверительного интервала:", lower_bound * 40 + 10)
print("Верхняя граница доверительного интервала:", upper_bound * 40 + 10)
"""
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta
alpha = 3
beta1 = 7
x = np.linspace(0, 1, 100)
pdf = beta.pdf(x, alpha, beta1)
plt.plot(x, pdf)
plt.xlabel('Значение')
plt.ylabel('Плотность вероятности')
plt.title('Бета-распределение (alpha={}, beta={})'.format(alpha, beta))
plt.show()
a = 3# параметр a бета-распределения
b = 7  # параметр b бета-распределения
dist = beta(a, b)  # создание объекта распределения бета
lower_bound = dist.ppf(0.025)
upper_bound = dist.ppf(0.975)
print("Нижняя граница доверительного интервала:", lower_bound)
print("Верхняя граница доверительного интервала:", upper_bound)
import numpy as np
import matplotlib.pyplot as plt
a = 30
b = 70
a1 = 20
b1 = 80
size = 100000  # размер выборки
samples = np.random.beta(a + 36, b + 114, size)
samples1 = np.random.beta(a1 + 50, b1 + 100, size)
def ecdf(data):
    n = len(data)
    x = np.sort(data)
    y = np.arange(1, n+1) / n
    return x, y
# Пример использования
data = np.array(samples / samples1)
x, y = ecdf(data)
print(x)  # Отсортированные значения данных
print(y)
plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.xlabel('Значение данных')
plt.ylabel('ECDF')
plt.title('Эмпирическая функция распределения (ECDF)')
plt.grid(True)
plt.show()
print(sum(samples1 > samples)/size)
"""
import numpy as np
a_true_rate = 0.25
b_true_rate = 0.3
prior_alpha = 300
prior_beta = 700
number_of_samples = 0
p_b_superior = -1
while p_b_superior < 0.95:
    number_of_samples += 100
    a_results = np.random.uniform(0, 1, size=int(number_of_samples/2)) <= a_true_rate
    b_results = np.random.uniform(0, 1, size=int(number_of_samples/2)) <= b_true_rate
    a_samples = np.random.beta(sum(a_results == True) + prior_alpha, sum(a_results == False) + prior_beta, size=number_of_samples)
    b_samples = np.random.beta(sum(b_results == True) + prior_alpha, sum(b_results == False) + prior_beta, size=number_of_samples)
    p_b_superior = np.sum(b_samples > a_samples) / number_of_samples

print("Number of samples:", number_of_samples)
print("p(b superior to a):", p_b_superior)