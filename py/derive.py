from math import *

def derivative(f, a):
    h = 1.0 * 10**(-10)
    x1 = a-h
    x2 = a+h
    y1 = f(x1)
    y2 = f(x2)
    Dya = (y2 - y1)/(x2 - x1)
    return (y2 - y1)/(x2 - x1)

if __name__ == "__main__":
    print(derivative(sin, 0))