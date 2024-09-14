#Write a script that renames all the files in a folder
#Give them a default name and an incrementing counter.

import pathlib

path = pathlib.Path.cwd()

count = 0

for file in path.iterdir():
    if file.is_file():
        renamed = "file_" + str(count) + file.suffix
        file.rename(path / renamed)
        count += 1