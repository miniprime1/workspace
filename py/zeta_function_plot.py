import matplotlib.pyplot as plt
import numpy as np
import mpmath as mp

x = np.arange(1.01, 10.00, 0.01)
y = []

for i in x: y.append(mp.zeta(i))

plt.plot(x, y, 'r', label='Riemann Zeta Function')
plt.legend(loc = "upper right")
plt.axis([0, 8, 0, 10])
plt.title("Plot of Riemann Zeta Function (x > 1)")
plt.show()