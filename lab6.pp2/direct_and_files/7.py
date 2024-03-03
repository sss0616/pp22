def copy(s, d):
    with open(s, 'r') as source:
        with open(d, 'w') as destination:
            for line in source:
                destination.write(line)

s = "path/to/source_file.txt"
d = "path/to/destination_file.txt"
copy(s, d)
