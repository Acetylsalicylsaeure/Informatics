a = 1
b = 3
i = 5

for n in range(i, 16):
    print(a-1, end=";")
    a += n**3+n*2+b*n
    b += 1
print(a)
