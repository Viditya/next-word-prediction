import os
from zipfile import ZipFile

file_dir = "book.zip"
out_dir = "data"

if os.path.exists(out_dir):
    print("File already zipped")
else:
    os.makedirs(out_dir)
    # loading the temp.zip and creating a zip object
    with ZipFile(file_dir, "r") as zObject:
        # Extracting all the members of the zip
        # into a specific location.
        zObject.extractall(path=out_dir)
