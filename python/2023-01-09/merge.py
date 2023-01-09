# todo: write function that merges 2 .txt files into newfile


def mergefile(file1, file2, newfile):
    with open(file1) as f1, open(file2) as f2:
        output = list(f1) + list(f2)
        print(output)


mergefile("Files/hours.txt", "Files/person.txt", "new")
