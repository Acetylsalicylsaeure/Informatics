a = int(input("please give the starting number from which to sum from: "))
b = int(input("please give the (exclusive) end number to sum to: "))
ssq = 0

for x in range(a, b):
    ssq += x**2

print("your sum of the squares is:", ssq)
