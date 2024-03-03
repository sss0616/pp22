import os

def test(path):
    if os.path.exists(path):
        print("path exists")
        directory, filename = os.path.split(path)
        print("directory", directory)
        print("filename", filename)
    else:
        print("path doesnt exist")
path = "path/to/your/file"
test(path)
