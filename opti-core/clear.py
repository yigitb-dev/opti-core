import os

class clear:
    def _init__(self,directory):
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
                            os.remove(item_path)  # Remove duplicate file
                            print(f"Removed duplicate: {item_path}")
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