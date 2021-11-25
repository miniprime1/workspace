import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-5, 5, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, 'b', x, y2, 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sample Graph')
plt.axis([-4, 4, -2, 2])
plt.legend(['Sine', 'Cosine'])
plt.grid('on')