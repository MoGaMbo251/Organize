import os
import shutil

# Define the paths for the source Downloads folder and the target organized folder
downloads_folder = "/path/to/your/friend/downloads"
organized_folder = "/path/to/organized/folder"

# Create the organized folder if it doesn't exist
if not os.path.exists(organized_folder):
    os.makedirs(organized_folder)

# Dictionary to map file extensions to their corresponding folders
file_types = {
    "pdf": "PDFs",
    "doc": "Documents",
    "docx": "Documents",
    "ppt": "Presentations",
    "pptx": "Presentations",
    "xls": "Spreadsheets",
    "xlsx": "Spreadsheets",
    "png": "Images",
    "jpg": "Images",
    "jpeg": "Images",
    "txt": "TextFiles",
    "zip": "Archives",
    "rar": "Archives",
    "exe": "Executables",
    # Add more file extensions and corresponding folders as needed
}

# Loop through each file in the Downloads folder
for filename in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, filename)
    if os.path.isfile(file_path):
        # Get the file extension
        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension[1:].lower()  # Remove the dot and convert to lowercase
        
        # Determine the target folder based on the file extension
        target_folder = os.path.join(organized_folder, file_types.get(file_extension, "Other"))
        
        # Create the target folder if it doesn't exist
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        
        # Move the file to the target folder
        target_path = os.path.join(target_folder, filename)
        shutil.move(file_path, target_path)
        print(f"Moved '{filename}' to '{target_folder}'")

print("Organizing completed.")
