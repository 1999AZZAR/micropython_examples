import os

def list_files_and_folders(directory_path):
    """
    List both files and folders within a specified directory.
    """
    try:
        items = os.listdir(directory_path)
        for item in items:
            item_path = directory_path + '/' + item
            if os.stat(item_path)[0] & 0x4000:  # Check if item is a directory
                print(f"Folder: {item}")
            else:
                print(f"File: {item}")
    except OSError as e:
        print(f"Error listing directory '{directory_path}': {e}")

# Example usage:
# Uncomment and adjust the parameter as needed
list_files_and_folders('/')  # Uncomment to list files and folders within the '/' or root directory
