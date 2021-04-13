import matplotlib.pyplot as plt
from scipy.special import gamma
import numpy as np

x = np.arange(-5.00, 5.00, 0.01)
y = gamma(x)

plt.plot(x, y, 'b', label='gamma(x)')
plt.legend(loc="upper right")
plt.axis([-5, 5, -10, 25])
plt.grid()
plt.show()