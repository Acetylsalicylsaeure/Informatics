inp = input("please input a list: ")
inp = inp.replace(" ", "")
list1 = inp.split(",")
output = []
print(list1)


for key in list1:
    if key not in output:
        output == output.append(key)

print(output)
