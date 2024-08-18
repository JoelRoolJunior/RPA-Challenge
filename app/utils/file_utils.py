import shutil

def read_text_file(file_path):
    """Read the contents of a text file and return it as a string."""
    with open(file_path, 'r') as file:
        return file.read()

def write_text_file(data, file_path):
    """Write a string to a text file."""
    with open(file_path, 'w') as file:
        file.write(data)

def copy_file(origin, destination):
    """Copy a file and its metadata from origin to destination"""
    shutil.copy2(origin, destination)

def move_file(origin, destination):
    """Move a file and its metadata from origin to destination."""
    shutil.move(origin, destination)