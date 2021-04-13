import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-10, 10, 0.01)
y1 = (x**2) * (1/2)
y2 = [1] * 2000
plt.plot(x, y1, 'b', label='Integral(x)')
plt.plot(x, y2, 'r', label='Derivative(x)')
plt.axis([-10, 10, 0, 50])
plt.title("Plot of Int/Diff")
plt.legend(loc = "upper right")
plt.grid()
plt.show()