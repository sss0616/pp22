def write(file_path, input_list):
    with open(file_path, 'w') as file:
        for item in input_list:
            file.write(str(item) + "\n")

file_path = "path/to/your/output_file.txt"
input_list = ["item1", "item2", "item3"]
write(file_path, input_list)
