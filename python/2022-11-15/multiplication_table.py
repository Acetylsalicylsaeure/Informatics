print("x |\t1,\t2,\t3,\t4,\t5,\t6,\t7,\t8,\t9,\t10")
print("---------------------------------------------------------------------"
      "--------------")
for x in range(1, 11):
    print(x, "|\t", end="")
    for y in range(1, 11):
        print(x*y, end="\t")
    print()
