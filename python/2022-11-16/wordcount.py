count = 1
string = "this is a string in which the \"words\" should be counted"

for x in string:
    if x == " ":
        count += 1

print("given string:", string)
print("there are {} words (=white spaces + 1) in the string".format(count))
