# Author: Md. Fahim Bin Amin
# License: Apache License


import os


def rename_nii_files(root_dir):
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.nii'):
                old_name = os.path.join(subdir, file)
                base_name, ext = os.path.splitext(file)
                parts = base_name.split('_')
                new_name = parts[-1] + ext
                new_name = os.path.join(subdir, new_name)
                os.rename(old_name, new_name)
                print(f"Renamed '{old_name}' to '{new_name}'.")


# Provide the root directory containing the AD, CN, and MCI subdirectories
root_directory = "."  # Change this to the actual root directory if it's different

# Run the function
rename_nii_files(root_directory)