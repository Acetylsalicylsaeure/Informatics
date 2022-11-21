# key:value pairs can be appended
dictionary = {}
dictionary["number"] = [1]
dictionary["string"] = "test"

print(dictionary)

# checks if a key is in the dictionary
if "number" in dictionary:
    print("'number' is in the dictionary")

# appends to a value, must be a list (e.g. no int)
dictionary["number"].append(34)
print("\n", dictionary, sep="")
