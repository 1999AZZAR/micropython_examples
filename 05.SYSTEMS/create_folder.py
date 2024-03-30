import os

def create_folder_root(folder_name):
    """
    Create a folder in the root directory.
    """
    if folder_name in os.listdir('/'):
        print(f"Folder '{folder_name}' already exists.")
    else:
        os.mkdir('/' + folder_name)
        print(f"Folder '{folder_name}' created successfully.")

def create_folder_in_directory(directory_path, new_folder_name):
    """
    Create a folder within a specified directory.
    """
    new_folder_path = directory_path + '/' + new_folder_name
    try:
        os.mkdir(new_folder_path)
        print(f"Folder '{new_folder_name}' created successfully in '{directory_path}'.")
    except FileExistsError:
        print(f"Folder '{new_folder_name}' already exists in '{directory_path}'.")

# Example usage:
# Uncomment and adjust the parameters as needed
# create_folder_root('lib')  # Uncomment to create a folder named 'lib' in the root directory
# create_folder_in_directory('/lib', 'my_folder')  # Uncomment to create a folder named 'my_folder' within the 'lib' folder
