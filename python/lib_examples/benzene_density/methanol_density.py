import numpy as np
import matplotlib.pyplot as plt

methanol_data = np.loadtxt("methanol.csv", delimiter="\t", skiprows=1,
                          usecols=(0, 2), unpack=True)

print(methanol_data)

methanol_data[0] = methanol_data[0] - 273.15

plt.plot(methanol_data[0], methanol_data[1])
plt.xlabel("Temperature ($^\circ$C)")
plt.ylabel("Density (mol/L)")
plt.title("methanol")
plt.show()
