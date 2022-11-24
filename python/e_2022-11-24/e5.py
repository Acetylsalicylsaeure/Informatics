my_dict = {
    'a b c': [2, 3, 5],
    'b d e': [1, 8, 4],
    'c f g': [9, 0, 1]
}
out_dict = dict()


for key in my_dict.keys():
    key2 = key.replace(" ", "")
    out_dict[key2] = my_dict[key]

print(out_dict)
