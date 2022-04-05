import os
import shutil

os.chdir("d:/Infrastucture")

# use copyfile()
shutil.copyfile('random.txt', 'random2.txt')

with open('random.txt', 'r') as f1, open('random2.txt', 'w') as f2:
    # read content from first file
    strings = ''
    for line in f1:
        for letter in line:

            if letter != " ":
                strings = strings + letter
            else:
                f2.write(f"{strings}\n")
                strings = ''

        if strings != "":
            f2.write(f"{strings}\n")