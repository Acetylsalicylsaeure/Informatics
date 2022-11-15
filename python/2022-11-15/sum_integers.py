a = int(input("please give the starting number from which to sum from: "))
b = int(input("please give the (exclusive) end number to sum to: "))
sum = 0

for x in range(a, b):
    sum += x

print("your sum is:", sum)
