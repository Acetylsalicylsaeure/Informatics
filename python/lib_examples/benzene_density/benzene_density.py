import numpy as np
import matplotlib.pyplot as plt

benzene_data = np.loadtxt("benzene.csv", delimiter="\t", skiprows=1,
                          usecols=(0, 2), unpack=True)

print(benzene_data)

benzene_data[0] = benzene_data[0] - 273.15

plt.plot(benzene_data[0], benzene_data[1])
plt.xlabel("Temperature ($^\circ$C)")
plt.ylabel("Density (mol/L)")
plt.title("Benzene")
plt.show()
