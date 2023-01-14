molecule = input("please enter your molecule as 'Cx Hx Nx Ox': ")


# defines dictionary to assign molecular weight
dic = {
    "C": 12.011,
    "H": 1.001,
    "N": 14.007,
    "O": 15.999
}


mass = 0
# splits input into list
l = molecule.split()

# for each list item, take the first value as dict key and multiply by
# following integer
for n in l:
    if len(n) < 2:
        n += "1"
    mass += dic[n[0]] * int(n[1:])


print(mass)
