import os

def create_file(filename):
    try:
        with open(filename, "w") as f:
            f.write("Hello World")
        print("File " + filename + " created successfully")
    except IOError:
        print("Could not create " + filename)

def rename_file(old_filename, new_filename):
    try:
        os.rename(old_filename, new_filename)
        print(f"Renamed {old_filename} to {new_filename} successfully")
    except FileNotFoundError:
        print(f"Error: Could not rename {old_filename} to {new_filename}")

def deletefile(filename):
    try:
        os.remove,(filename)
        print("Deleted successfully")
    except IOError:
        print("Error could not delete file" + filename)

if __name__ == "__main__":
    filename = "example.txt"
    new_filename = "new_Example.txt"
    create_file(filename)
    rename_file(filename,new_filename)
    deletefile(new_filename)