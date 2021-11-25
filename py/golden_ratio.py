import matplotlib.pyplot as plt
import numpy as np

n1 = 0
n2 = 1

phi = (1+np.sqrt(5))/2
frs = []

for i in range(16):
  nth = n1 + n2
  n1 = n2
  n2 = nth
  frs.append(n2/n1)

x = np.arange(1, 16+1)
y1 = frs
y2 = [phi] * 16

plt.plot(x, y1, 'g-o', label='Fibonacci Ratio Sequence')
plt.plot(x, y2, 'c-', label='Golden Ratio (1.618034...)')
plt.axis([1, 16, 0.5, 2.5])
plt.legend(loc='upper right')
plt.grid()
plt.show()