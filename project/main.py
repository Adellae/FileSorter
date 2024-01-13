import os
import getpass
from sorter.file_sorter import sort_downloads_folder

# Defining the download folder path
def downloads_folder_exists():
    if os.path.exists('project\\config\\user_defined_path.txt'):
        with open('project\\config\\user_defined_path.txt', 'r') as file:
            return file.read()
    else:
        username = getpass.getuser()
        download_folder = os.path.join('C:\\Users', username, 'Downloads')
        with open('project\\config\\user_defined_path.txt', 'w') as file:
            file.write(download_folder)
        return download_folder


if __name__ == "__main__":
    sort_downloads_folder(downloads_folder_exists())