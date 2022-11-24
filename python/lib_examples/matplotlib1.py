import matplotlib.pyplot as plt
import numpy as np

# defines an array as function y = x^2
x = np.arange(1, 11)
y = x**2

# plots and shows the plot (suprise!)
plt.plot(x, y)
plt.show()

# plots individual points with dotted line and o marker
# all markers can be found unter
# https://matplotlib.org/stable/api/markers_api.html
plt.plot(x, y, "o:")

# label the axes
plt.xlabel("x")
plt.ylabel("y^2")
plt.title("y = x^2")
plt.show()

# multiple lines in one plot
z = np.sqrt(x)
plt.plot(x, y, "o-", label="x^2")
plt.plot(x, z, "^--", label="sqrt(x)")
plt.plot(x, x, label="x")
plt.xlabel("x")
plt.ylabel("y")
plt.title("y=f(x)")
# shows legend
plt.legend()
plt.show()
