import numpy as np
import matplotlib.pyplot as plt


def attractive(dr, b):
    return -b / np.power(dr, 6)


def repulsive(dr, a):
    return a / np.power(dr, 12)


def lj(dr, constants):
    return repulsive(dr, constants[0]) + attractive(dr, constants[1])


r = np.linspace(3e-10, 8e-10, 100)
plt.plot(r, attractive(r, 9.273e-78), label='Attractive')
plt.plot(r, repulsive(r, 1.363e-134), label='Repulsive')
plt.plot(r, lj(r, [1.363e-134, 9.273e-78]), label='Lennard-Jones')
plt.xlabel('$r_{ij}$/m')
plt.ylabel('$E$/J')
plt.legend()
plt.show()
