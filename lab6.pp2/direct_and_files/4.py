def count(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return len(lines)
file_path = "path/to/your/file.txt"
print(count(file_path))
