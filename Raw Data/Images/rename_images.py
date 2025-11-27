import os
import re

def rename_files(directory, start_page):
    print(f"Starting to rename files in directory: {directory}")

    files = [f for f in os.listdir(directory) if f.lower().endswith('.jpg')]

    # Sort files based on the number
    def sort_key(filename):
        match = re.search(r'_(\d+)\.jpg$', filename)
        if match:
            return int(match.group(1))
        return float('inf') 

    files.sort(key=sort_key)

    for index, old_filename in enumerate(files):
        new_page_number = start_page + index
        new_filename = f"page_{new_page_number}.jpg"

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
        start_page = input("Enter the starting page number: ").strip()

        if start_page.isdigit():
            start_page = int(start_page)
            rename_files(folder, start_page)
        else:
            print("Error: Starting page must be a positive integer.")
    else:
        print(f"Error: The folder '{folder}' does not exist. Please check the path again.")

