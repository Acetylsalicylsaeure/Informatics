import csv
import statistics


numbers = []

# gets data into thenumbers list
with open("data.csv", "r") as file:
    data = csv.reader(file)
    for row in data:
        numbers.append(row[2])

# remove header
del numbers[0]

# get numbers into float
floats = []
for n in numbers:
    floats.append(float(n))

mean = statistics.mean(floats)
stdev = statistics.stdev(floats)

print(f"the data has a mean of {mean} and a standard deviation of {stdev}")
