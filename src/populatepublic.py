import os, shutil


# def populate_public():
#     shutil.copytree("static", "public", dirs_exist_ok=True)

def populate_public(directory):
    # First, remove the public directory if it exists
    if os.path.exists(directory):
        shutil.rmtree(directory)
    
    # Create a fresh public directory
    os.mkdir(directory)
    
    # Start the recursive copy
    copy_directory("static", directory)

def copy_directory(source, destination):
    # List all files and directories in the source
    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        dest_path = os.path.join(destination, item)
        
        # If it's a file, copy it
        if os.path.isfile(source_path):
            print(f"Copying file: {source_path} to {dest_path}")
            shutil.copy(source_path, dest_path)
        # If it's a directory, create it and recursively copy its contents
        else:
            print(f"Creating directory: {dest_path}")
            os.mkdir(dest_path)
            copy_directory(source_path, dest_path)