# Project 2: Automatic File Organizer

This project is a Python script that organizes files in a specified directory by moving them into subdirectories based on their file extension. For example, `.jpg` and `.png` files are moved to an `Images` folder, while `.pdf` and `.docx` files go into a `Documents` folder.

## Features
- Scans a target directory for files.
- Identifies file types by their extension.
- Creates new folders for different file categories if they don't exist.
- Moves files into the appropriate category folder.
- Files with uncategorized extensions are moved to an `Other` folder.

## Libraries Used
- `pathlib`: A modern, object-oriented way to handle filesystem paths (part of Python's standard library).
- `shutil`: For high-level file operations like moving files (part of Python's standard library).

## Setup & How to Run
1.  **Create a Target Directory:** In the same directory as the script, create a folder named `source_directory`.

2.  **Add Files:** Place a variety of files inside `source_directory` to test the script (e.g., `test.txt`, `image.jpg`, `document.pdf`, `archive.zip`).

3.  **Run the Script:** Navigate to this directory in your terminal and run the script:
    ```
    python organizer.py
    ```

After running, check the `source_directory`. You will find that your files have been neatly organized into new subfolders like `Documents`, `Images`, `Audio`, etc.