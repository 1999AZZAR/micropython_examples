import os

def delete_folder_root(folder_name):
    """
    Delete a folder in the root directory.
    """
    folder_path = '/' + folder_name
    if folder_name in os.listdir('/'):
        try:
            os.rmdir(folder_path)
            print(f"Folder '{folder_name}' deleted successfully.")
        except OSError as e:
            print(f"Error deleting folder '{folder_name}': {e}")
    else:
        print(f"Folder '{folder_name}' does not exist.")

def delete_folder_in_directory(directory_path, folder_name):
    """
    Delete a folder within a specified directory.
    """
    folder_path = directory_path + '/' + folder_name
    if folder_name in os.listdir(directory_path):
        try:
            os.rmdir(folder_path)
            print(f"Folder '{folder_name}' deleted successfully from '{directory_path}'.")
        except OSError as e:
            print(f"Error deleting folder '{folder_name}' from '{directory_path}': {e}")
    else:
        print(f"Folder '{folder_name}' does not exist in '{directory_path}'.")

# Example usage:
# Uncomment and adjust the parameters as needed
# delete_folder_root('lib')  # Uncomment to delete the 'lib' folder from the root directory
# delete_folder_in_directory('/lib', 'my_folder')  # Uncomment to delete the 'my_folder' folder within the 'lib' folder
