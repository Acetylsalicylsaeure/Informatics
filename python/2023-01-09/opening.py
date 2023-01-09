# imports os lib
import os
# sets current dir
currentdir = os.path.dirname(__file__)
print(currentdir)
# conveniently saves path for subfiles
newpath = currentdir + "/Files/"

# opens txt file as read and prints it
f = open(newpath+"hours.txt", "r")
print(f.read())
# closes file so that it doesn't hog memory
f.close()
# print(f.read()) would now give an I/O closed file error

f2 = open(newpath+"hours.txt")
# reads a single line from file
print(f2.readline())
f2.close()

f3 = open(newpath+"hours.txt")
# reads all the lines and outputs as seperate list items
data = f3.readlines()
print(data)
# strips the whitespace and prints as seperate lines
for line in data:
    print(line.strip())
f3.close()
