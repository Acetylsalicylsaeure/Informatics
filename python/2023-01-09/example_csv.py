# imports csv lib
import csv

# opens file
with open("Files/test.csv", "r") as f:
    # reads csv file
    content = csv.reader(f, delimiter=";")
    listed = list(content)
    print(listed)

    # acess grades by name input
    query = input("please enter the name of the student: ")
    # enumerate() gives out 2 values for for loops, i=index & n=list item
    for i,n in enumerate(listed):
        if n[0] == query:
            print(f"the final grade of {query} is {n[4]}")
