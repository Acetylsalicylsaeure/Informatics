# my admittedly somewhat simplistic solution to printing every 2nd list item
list2 = range(1, 21)
list1 = []
count = 1

for i in list(list2):
    if count%2 == 0:
        list1.append(i)
        count += 1
    else:
        count += 1

print(list(list1))
