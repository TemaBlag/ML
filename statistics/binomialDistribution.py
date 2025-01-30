import matplotlib.pyplot as plt

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def b(k, n, p, flag=False):
    c = factorial(n)/(factorial(n - k) * factorial(k))
    res = c * pow(p, k) * pow((1-p), n-k)
    y = []
    a = 0
    for x in range(1, n + 1):
        c = factorial(n) / (factorial(n - x) * factorial(x))
        a = c * pow(p, x) * pow((1 - p), n - x)
        y.append(a)
    ks = list(range(1, n + 1))
    plt.plot(ks, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Пример графика')
    plt.show()
    if flag:
        return sum(y[k:])
    return res


print(b(1, 25, 0.1, flag=True))