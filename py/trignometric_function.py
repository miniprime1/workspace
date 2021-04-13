import matplotlib.pyplot as plt
import numpy as np
t = np.arange(-2*np.pi, 2*np.pi, 0.01)
y1 = np.sin(t) # sine
y2 = np.cos(t) # cosine
y3 = np.tan(t) # tangent
y4 = np.cos(t) / np.sin(t) # cotangent
y5 = 1 / np.cos(t) # secant
y6 = 1 / np.sin(t) # cosecant
plt.plot(t, y1, 'b', label='sin(t)')
plt.plot(t, y2, 'r', label='cos(t)')
plt.plot(t, y3, 'y', label='tan(t)')
plt.plot(t, y4, 'm', label='cot(x)')
plt.plot(t, y5, 'g', label='sec(t)')
plt.plot(t, y6, 'c', label='csc(t)')
plt.axis([-2*np.pi, 2*np.pi, -4, 4])
plt.title("Plot of Trigonometric Functions")
plt.legend(loc = "upper right")
plt.show()
# plt.savefig("trignometric_function.png")