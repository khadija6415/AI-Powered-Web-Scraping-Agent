
import zipfile

# Specify the path to the zip file
zip_file_path = '/content/archive.zip'

# Open the zip file in read mode
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    # Extract all the contents into the current directory
    zip_ref.extractall('./')

print("Archive extracted successfully!")
