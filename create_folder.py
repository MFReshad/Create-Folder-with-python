import os

# Specify the path where you want to create the folders (change to your desired path)
folder_path = "E:/Cse/4.2/CSE 4227 - Digital Image Processing/Lectures/"

# Create 11 folders and rename them
for i in range(1, 12):
    # Generate folder name
    folder_name = f"Chapter - {i:02d}"  # Using :02d to format the number with leading zeros if needed

    # Combine the path and folder name to create the full folder path
    full_folder_path = os.path.join(folder_path, folder_name)

    # Check if the folder already exists
    if not os.path.exists(full_folder_path):
        # Create the folder along with any missing parent directories
        os.makedirs(full_folder_path)
        print(f"Folder '{folder_name}' created successfully.")
    else:
        print(f"Folder '{folder_name}' already exists.")
