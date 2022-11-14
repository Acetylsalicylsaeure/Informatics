n = 0
keepGoing = "y"

while keepGoing == "y":
    keepGoing = input("please input \"y\" to count: ")
    if keepGoing == "y":
        n += 1
        print(n)
