# get input
n = int(input("Please enter a number: "))
factorial = n
m = n

# evaluate input
if n <= 0:
    print("Please enter a positive integer")
    quit()

# calculate factorial
while n > 1:
    n -= 1
    factorial *= n

# output result
print("Product of first {} numbers is".format(m), factorial)
