import os

os.chdir("../Images")

files = os.listdir()

for file in files:

    print(file)