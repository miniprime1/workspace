import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-2*np.pi, 2*np.pi, 0.01)
y = np.abs(x)
plt.plot(x, y, label='abs(x)')
plt.axis([-4, 4, -0.5, 4.0])
plt.title("Plot of Absolute Value")
plt.legend(loc = "upper right")
plt.grid()
plt.show()