import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-5, 5, 0.01)
y1 = 1*x
y2 = 1/x
y2[500] = None
plt.plot(x, y1, label='Direct Proportion')
plt.plot(x, y2, label='Inverse Proportion')
plt.axis([-4, 4, -4, 4])
plt.legend(loc = "upper right")
plt.title("Proportion Graph")
plt.grid()
plt.show()