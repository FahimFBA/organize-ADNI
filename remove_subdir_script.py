# Author: Md. Fahim Bin Amin
# License: Apache License


import os
import shutil


# Function to move .nii files and remove empty subdirectories
def process_directories():
    root_dirs = ['AD', 'CN', 'MCI']
    for root_dir in root_dirs:
        root_path = os.path.join(os.getcwd(), root_dir)
        if not os.path.exists(root_path):
            print(f"Directory '{root_dir}' not found.")
            continue

        for subdir, _, files in os.walk(root_path):
            nii_files = [f for f in files if f.endswith('.nii')]
            for nii_file in nii_files:
                src_path = os.path.join(subdir, nii_file)
                dest_path = os.path.join(root_path, nii_file)
                shutil.move(src_path, dest_path)
                print(f"Moved '{nii_file}' to '{root_dir}' directory.")

        # Remove empty subdirectories
        for dirpath, dirnames, filenames in os.walk(root_path, topdown=False):
            for dirname in dirnames:
                full_dirpath = os.path.join(dirpath, dirname)
                if not os.listdir(full_dirpath):
                    os.rmdir(full_dirpath)
                    print(f"Removed empty directory: '{full_dirpath}'.")


# Run the function
process_directories()