text = input("please enter your text: ")
sep = input("please enter your desired seperator: ")
output = ""

for n in text:
    output = output + n + sep
output = output.strip(sep)

for n in text:
    print(output)
    output = output.strip(sep + output[-0])
print(output)
