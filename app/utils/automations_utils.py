from pathlib import Path

def create_directory(path):
    if not Path.exists(path):
        Path.mkdir(path)

def remove_file(file_path):
    if not Path.exists(file_path):
        Path.unlink(file_path)

def delete_temp_files():
    temp_folder = Path.cwd() / 'temp'
    files = temp_folder.iterdir()
    for file in files:
        Path.unlink(file, True)
