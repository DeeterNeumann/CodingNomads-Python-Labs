# Write a script that walks through a nested folder structure
# Prints out all the Python files that it can find

import pathlib

file_path = pathlib.Path("/Users/drneu/Documents/CodingNomads/Labs")

for file in file_path.iterdir():
    if file.suffix == ".py":
        print(file.name)
    elif file.is_dir():
        for sub_file_path in file.iterdir():
            if sub_file_path.suffix == ".py":
                print(sub_file_path.name)