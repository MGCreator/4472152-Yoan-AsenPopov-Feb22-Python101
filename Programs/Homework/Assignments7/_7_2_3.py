import os

os.chdir("d:/Infrastucture")
command = input("Input a name: ")
with open('names.txt', 'w') as f:
    while command != "":
        f.write(f"{command}\n")
        command = input("Input a name: ")