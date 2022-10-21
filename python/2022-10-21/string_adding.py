string = "Abcdefghij"
length = len(string) // 2
if len(string) % 2 == 1:
    print(string[length - 1:length + 2])
else:
    print("sorry, due to an even string thength, no middle 3 characters can be\
given")
