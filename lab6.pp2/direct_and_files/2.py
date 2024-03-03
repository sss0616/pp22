import os

def check(path):
    if os.path.exists(path):
        print("path exists")
        print("readable", os.access(path, os.R_OK))
        print("writable", os.access(path, os.W_OK))
        print("executable", os.access(path, os.X_OK))
    else:
        print("path doesnt exist")
path = "path/to/your/directory"
check(path)
