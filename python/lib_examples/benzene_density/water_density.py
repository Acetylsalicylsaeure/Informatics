import numpy as np
import matplotlib.pyplot as plt

water_data = np.loadtxt("water.csv", delimiter="\t", skiprows=1,
                          usecols=(0, 2), unpack=True)

print(water_data)

water_data[0] = water_data[0] - 273.15

plt.plot(water_data[0], water_data[1])
plt.xlabel("Temperature ($^\circ$C)")
plt.ylabel("Density (mol/L)")
plt.title("Water")
plt.show()
