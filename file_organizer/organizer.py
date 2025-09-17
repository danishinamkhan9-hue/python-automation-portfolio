# file_organizer/organizer.py

import pathlib
import shutil

def organize_files(source_path_str):
    """
    Organizes files in the source directory into subdirectories based on file type.

    Args:
        source_path_str (str): The path to the directory to be organized.
    """
    source_path = pathlib.Path(source_path_str)

    # Check if the source directory exists
    if not source_path.exists() or not source_path.is_dir():
        print(f"Error: The source directory '{source_path_str}' does not exist.")
        print("Please create it and add some files to organize.")
        return

    # Define file type categories and their corresponding extensions
    FILE_CATEGORIES = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
        'Audio': ['.mp3', '.wav', '.aac', '.flac'],
        'Video': ['.mp4', '.mov', '.avi', '.mkv'],
        'Archives': ['.zip', '.rar', '.tar', '.gz']
    }

    print(f"Starting to organize files in: {source_path.resolve()}")

    # Iterate over all items in the source directory
    for item_path in source_path.iterdir():
        # Skip directories and process only files
        if item_path.is_file():
            file_extension = item_path.suffix.lower()
            
            # Determine the destination folder for the current file
            destination_folder_name = 'Other' # Default category
            for category, extensions in FILE_CATEGORIES.items():
                if file_extension in extensions:
                    destination_folder_name = category
                    break
            
            # Create the full path for the destination folder
            destination_path = source_path / destination_folder_name
            
            # Create the destination folder if it doesn't exist
            destination_path.mkdir(exist_ok=True)
            
            # Move the file to the destination folder
            try:
                shutil.move(str(item_path), str(destination_path))
                print(f"Moved: {item_path.name} -> {destination_folder_name}/")
            except Exception as e:
                print(f"Error moving {item_path.name}: {e}")

    print("\nFile organization complete!")


# --- Main Execution ---
if __name__ == "__main__":
    # The name of the directory to be organized.
    # The script expects this directory to be in the same folder as the script itself.
    SOURCE_DIRECTORY = 'source_directory'
    organize_files(SOURCE_DIRECTORY)
