import os
import shutil

def get_category(file_type):
    image_types = ['jpg', 'jpeg', 'png', 'gif', 'bmp']
    video_types = ['mp4', 'mkv', 'avi', 'mov', 'wmv']
    document_types = ['pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx']
    executable_types = ['exe', 'msi', 'bat', 'sh']

    if file_type in image_types:
        return 'Images'
    elif file_type in video_types:
        return 'Videos'
    elif file_type in document_types:
        return 'Documents'
    elif file_type in executable_types:
        return 'Executables'
    else:
        return 'Others'


def sort_downloads_folder(downloads_path):
    for filename in os.listdir(downloads_path):
        # Get Downloads folder path dynamically
        file_path = os.path.join(downloads_path, filename)

        # Check to only move files, not existing directories
        if os.path.isfile(file_path):
            file_type = filename.split('.')[-1].lower()
            category = get_category(file_type)

            destination_folder = os.path.join(downloads_path, category)

            # Create a folder for the category if it doesn't exist
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            destination_path = os.path.join(destination_folder, filename)

            # Move the file to the appropriate folder
            shutil.move(file_path, destination_path)
            print(f"Moved {filename} to {destination_folder}")