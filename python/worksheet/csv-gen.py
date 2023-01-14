import random
import csv


filename = "data.csv"
fields = ["name", "count", "data", "random"]

with open(filename, "w") as file:
    #generate writer object
    csvwriter = csv.writer(file)

    #write header
    csvwriter.writerow(fields)

    #loop to write data
    for n in range(0, 100):
        csvwriter.writerow(["", n, random.gauss(187.5, 5.3),
                            random.randrange(1, 99)])
