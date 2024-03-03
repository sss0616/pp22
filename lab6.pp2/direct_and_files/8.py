import os
def dele(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print("deleted")
        else:
            print("no, write access")
    else:
        print("doesnt exist")

file_path = "path/to/your/file.txt"
dele(file_path)
