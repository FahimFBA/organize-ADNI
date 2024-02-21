# Author: Md. Fahim Bin Amin
# License: Apache License


import os
import csv
import shutil

# Function to move folders based on group


def move_folders(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            subject = row['Subject']
            group = row['Group']
            if group in ['MCI', 'AD', 'CN']:
                source_folder = os.path.join(os.getcwd(), subject)
                destination_folder = os.path.join(os.getcwd(), group)
                if os.path.exists(source_folder) and os.path.exists(destination_folder):
                    shutil.move(source_folder, destination_folder)
                    print(f"Moved folder '{subject}' to '{group}' folder.")
                else:
                    print(f"Source or destination folder does not exist for '{subject}' or '{group}'. Skipping.")


# Run the function
# change the file name to your csv file
move_folders('ADNI1_Screening_1.5T_1_29_2024.csv')
