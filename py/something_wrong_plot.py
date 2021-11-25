import matplotlib.pyplot as plt
import numpy as np

def sin(x): return np.sin(x)
def cos(x): return np.cos(x)
def tan(x): return np.tan(x)
def cot(x): return 1/np.tan(x)
def sec(x): return 1/np.cos(x)
def csc(x): return 1/np.sin(x)

x = np.arange(-2*np.pi, 2*np.pi, 0.01)
y = sin(cos(tan(cot(sec(csc(x))))))

plt.plot(x, y, 'r', label='sin(cos(tan(cot(sec(csc(x))))))')
plt.legend(loc="upper right")
plt.title("Something Wrong Plot")
plt.axis([-2*np.pi, 2*np.pi, -1.5, 1.5])
plt.grid()
plt.show()