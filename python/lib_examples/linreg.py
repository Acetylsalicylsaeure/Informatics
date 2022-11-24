import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

x = np.arange(1, 101)
offset = 20
y = x + (np.random.rand(100) - 0.5) * offset

# store linear regression
slope, intercept, rvalue, pvalue, stderr = linregress(x, y)
y_fit = slope * x + intercept

plt.plot(x, y, "o")
plt.plot(x, y_fit)
plt.xlabel("x")
plt.ylabel("y")

title = "y = {}x + {}".format(slope, intercept)
plt.title(title)
plt.show()
print(linregress(x, y))
