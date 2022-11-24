import numpy as np

a = np.arange(1, 51)
print(a)
print(np.min(a))
print(np.max(a))
print(np.sum(a))

print("mean of a =", np.sum(a)/len(a))
# alternative
print("mean of a =", np.mean(a))

print("standard deviation of a =", np.std(a))
