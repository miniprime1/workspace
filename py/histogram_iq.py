import matplotlib.pyplot as plt
import numpy as np

mu = 100
sigma = 15
x = mu + sigma * np.random.randn(10000)
num_bins = 20

plt.hist(x, num_bins, facecolor='blue', alpha=0.5)
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

plt.subplots_adjust(left=0.15)
plt.show()