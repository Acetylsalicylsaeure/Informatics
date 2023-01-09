file = open("newfile.txt", "w")
file.write("this is a file in which we are writing some very valuable info")
file.write("\nthis is a new line\n")
file.close()

# we confirm that we have written into the file
f2 = open("newfile.txt", "r")
print(f2.read())
f2.close()

# open and close file in one function, good form
with open("Files/hours.txt") as file:
    for line in file:
        print(line)
