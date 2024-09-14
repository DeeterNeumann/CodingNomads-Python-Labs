# Write a script that moves all files with the .png extension
# from one folder to another

# Import pathlib

# Find the path to my Desktop

# Create a new folder

# Filter for screenshots only

# Create a new path for each file

# Move the screenshot there

import pathlib

drneu = pathlib.Path("/Users/drneu")

new_path = pathlib.Path("/Users/drneu/screenshots")
new_path.mkdir(exist_ok=True)

for filepath in drneu.iterdir():
    if filepath.suffix == ".png":
        new_filepath = new_path.joinpath(filepath.name)
        filepath.replace(new_filepath)