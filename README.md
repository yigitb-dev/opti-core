# opti-core

`opti-core` is a Python library designed to help you manage and optimize your file system. It provides tools to clear duplicate files, remove empty folders, and organize files in a structured way.

## Features

- **Clear Duplicate Files**: Automatically scans directories to find and remove duplicate files.
- **Remove Empty Folders**: Cleans up empty folders from your directory structure.
- **Organize Downloads**: Sorts files in the `Downloads` folder by their file types into categorized subfolders.


## Usage
- **Clear Files and Folders
- **Use the clear class to clean up your directory:
```bash
from opti_core.organize import organize

directory = "path/to/your/directory"
users = ["user1", "user2"]  # Replace with actual usernames
organizer = organize(directory, users)
organizer.downloads_organizer()
```

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/opti-core.git
```


