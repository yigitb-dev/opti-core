import os
import shutil

class clear:
    def __init__(self,directory):
        self.directory = directory

        def scan_and_remove_duplicates():
            items = os.listdir(self.directory)
            seen = set()

            # Check if there are subdirectories
            has_subdirs = False
            for item in items:
                item_path = os.path.join(directory, item)
                if os.path.isdir(item_path):
                    has_subdirs = True
                    scan_and_remove_duplicates(item_path)  # Recursive function to go all the way in LOVE MR TRUYENS

            #Remove files after check 
            if not has_subdirs:
                for item in items:
                    item_path = os.path.join(directory, item)
                    if os.path.isfile(item_path):  #Dont touch folders
                        if item in seen:
                            shutil.move(item_path,"C:\\$Recycle.Bin\\")  # Remove duplicate file
                            print(f"Moved duplicate to Recylcle Bin: {item_path}")
                        else:
                            seen.add(item)
            
        #Function to remove empty folders
        def remove_folders(directory):
            items = os.listdir(directory)
            if items == []:
                os.rmdir(directory)
            for item in items:
                item_path = os.path.join(directory,item)
                if os.path.isdir(item_path):
                    remove_folders() #Recursive function to go all the way in LOVE MR TRUYENS
        
        def empty_trash():
            recycle_bin = "C:\\$Recycle.Bin\\"
            for item in os.listdir(recycle_bin):
                item_path = os.path.join(recycle_bin, item)
                os.remove(item_path)
