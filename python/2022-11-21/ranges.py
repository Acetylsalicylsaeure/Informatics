range1 = range(1, 5)
range2 = range(10, 15)

for i in (list(range1) + list(range2)):
    print(i)

print(list(range1) + list(range2))
