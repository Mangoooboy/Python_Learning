import os

old_name = "../Images/image_1.jpg"

new_name = "../Images/capture_1.jpg"

os.rename(old_name, new_name)

print("File Renamed Successfully")