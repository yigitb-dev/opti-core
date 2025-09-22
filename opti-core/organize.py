import shutil
import os

class organize:
    def __init__(self,directory,users_folder):
        self.directory = directory
        self.users = users_folder
    
    def downloads_organizer():
        for user in self.users:
            downloads_path = os.path.join(r"C:\Users", user, "Downloads")
            if os.path.exists(downloads_path):
                files = os.listdir(downloads_path)
                print(f"Contents of {downloads_path}: {files}")

                for file in files:
                    file_type = os.path.splitext(file)[1][1:]
                    folder_path = os.path.join(downloads_path, file_type)
                    if not os.path.exists(folder_path):
                        os.mkdir(folder_path)
                    shutil.move(os.path.join(downloads_path, file), os.path.join(folder_path, file))