# declaring empty lists
list1 = list()
list2 = []

list3 = [1, 2, 3, 4, "blue", "ball"]
# adds list3 into list4
list4 = ["test"] + list3

# adds 1 item to list
list2.append("this is text")

# adds list to other list
list1.extend(list3)

print(list1, list2, list3, list4, sep="\n")
print(list3[4:6], "each time she says 'blue ball' i manually shorten my"
      "lifespan by 5 minutes.")
