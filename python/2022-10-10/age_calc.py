import datetime
#imports library to read current date

age = int(input("How old are you? "))
# user input for age calculation

date = datetime.date.today()
year = date.strftime("%Y")
# saves current year as variable

birthyear = int(year) - age
# calculates birthyear, prints it
print("You were born in", birthyear)
