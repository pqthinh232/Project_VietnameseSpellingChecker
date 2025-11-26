import os
import re

def rename_files(directory):
    print(f"Starting to rename files in directory: {directory}")

    # Get all .jpg files in the directory
    files = [f for f in os.listdir(directory) if f.lower().endswith('.jpg')]

    # Sort files based on the number at the end of their names (e.g., _1, _2, _3)
    def sort_key(filename):
        match = re.search(r'_(\d+)\.jpg$', filename)
        if match:
            return int(match.group(1))
        return float('inf')  # Push unmatched files to the end

    files.sort(key=sort_key)

    # Rename files sequentially
    for index, old_filename in enumerate(files):
        new_filename = f"page_{index + 1}.jpg"

        old_path = os.path.join(directory, old_filename)
        new_path = os.path.join(directory, new_filename)

        if old_filename != new_filename:
            try:
                os.rename(old_path, new_path)
                print(f"Renamed: {old_filename} -> {new_filename}")
            except Exception as e:
                print(f"Error renaming {old_filename}: {e}")
        else:
            print(f"{old_filename} is already in the correct format.")

if __name__ == "__main__":
    folder = input("Enter the folder name containing the images: ").strip()

    if os.path.isdir(folder):
        rename_files(folder)
    else:
        print(f"Error: The folder '{folder}' does not exist. Please check the path again.")
