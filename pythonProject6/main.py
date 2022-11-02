import numpy as np
import matplotlib.pyplot as plt
import math


def f(x: float) -> float:
    return math.sin(x)


def b1(x: float) -> float:
    if abs(x) <= 1:
        return 1 - abs(x)
    else:
        return 0


def x_vec(a: float, b: float, n: int) -> np.ndarray:
    h = (b - a) / n
    return np.array([a + k * h for k in range(n+1)])


# def y_vec(a: float, b: float, n: int) -> np.ndarray:
    #  return np.array([f(x) for x in x_vec(a, b, n)])


def s_1(a: float, b: float, n: int, x: float) -> float:
    s1 = 0
    h = (b - a) / n
    xs = x_vec(a, b, n)
    for i in range(n+1):
        s1 += f(xs[i]) * b1((x - xs[i]) / h)
    return s1


# Visualization
def draw_plot(a: float, b: float, n: int, m: int = 500):
    x_to_plot = np.linspace(a, b, num=m)
    y_func = np.array([f(x) for x in x_to_plot])
    s1_func = np.array([s_1(a, b, m, x) for x in x_to_plot])

    plt.plot(x_to_plot, y_func, 'k-', label="f(x)")
    plt.plot(x_to_plot, s1_func, 'r-', label=f"$S_1(x)$")

    plt.legend(loc='best')
    plt.show()


def main():
    n = int(input("Enter n: "))  # на скільки частин розбивається відрізок
    while n <= 0:
        n = int(input("Enter valid n: "))
    # a = float(input("Enter a: "))
    # b = float(input("Enter b: "))
    a = -3
    b = 3
    x = float(input("Enter xє[a,b]: "))
    s_1(a, b, n, x)
    y_error = abs(f(x) - s_1(a, b, n, x))
    print(f"Error at x={x}: {y_error}")
    draw_plot(a, b, n)


if __name__ == '__main__':
    main()







