example_list = [1, 2, 3, "four", 5, 6.0]

# prints index 1 & 2
print(example_list[1:3])

# prints index total-3 til end
print(example_list[-3:])

# prints index 0 til total-3
print(example_list[:-3])

# prints index 3
print(example_list[3])


# create slice object, basically range of list
s1 = slice(1, 3)
# print only s1 slice of example_list
print(example_list[s1])
