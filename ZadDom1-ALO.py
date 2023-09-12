import matplotlib.pyplot as plt
import numpy as np

def funkcja(x):
    return x**3

def wykres(a, b, r):
    x = np.linspace(a, b, r)
    y = funkcja(x)
    plt.plot(x, y, color='b')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend()
    plt.show()

wykres(-10, 10, 400)
