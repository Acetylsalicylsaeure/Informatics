import matplotlib.pyplot as plt
import numpy as np


# import the data from .csv file
lab1 = np.loadtxt('aChem lab5_1.csv', skiprows=1, usecols=(0, 1), unpack=True,
                 delimiter=",")
# calculate the pH difference per step
lab1_d = np.diff(lab1[1])
# add 0 value to front to adjust array size do equal sizes
lab1_d = np.insert(lab1_d, 0, [0], axis=0)
print(lab1_d)


lab2 = np.loadtxt('aChem lab5_2.csv', skiprows=1, usecols=(0, 1), unpack=True,
                 delimiter=",")
lab2_dpH = np.diff(lab2[1])
# divide pH change through unequal volume additions
lab2_dV = np.diff(lab2[0])
lab2_d = lab2_dpH / lab2_dV
lab2_d = np.insert(lab2_d, 0, [0], axis=0)
print(lab2_d)


lab3 = np.loadtxt('aChem lab5_3.csv', skiprows=1, usecols=(0, 1), unpack=True,
                 delimiter=",")
lab3_dpH = np.diff(lab3[1])
lab3_dV = np.diff(lab3[0])
lab3_d = lab3_dpH / lab3_dV
lab3_d = np.insert(lab3_d, 0, [0], axis=0)
print(lab3_d)


# plot and print all the results
plt.plot(lab1[0], lab1[1], "o", label="#1", color="tab:blue")
plt.plot(lab1[0], lab1_d, "o:", label="#1 pH change", color="tab:blue")

plt.plot(lab2[0], lab2[1], "o", label="#2", color="tab:orange")
plt.plot(lab2[0], lab2_d, "o:", label="#2 pH change", color="tab:orange")

plt.plot(lab3[0], lab3[1], "o", label="#3", color="tab:purple")
plt.plot(lab3[0], lab3_d, "o:", label="#3 pH change", color="tab:purple")

plt.legend()
plt.show()





