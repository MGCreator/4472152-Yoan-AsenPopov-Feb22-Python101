import os

print(os.getcwd())

os.chdir("d:/Infrastucture")

print(os.listdir())

os.mkdir("new folder for python")
os.chdir("new folder for python")
os.mkdir("my second folder")

try:
    os.rmdir("new folder for python")
except FileNotFoundError as err:
    print(f"Change the current working directory. Error: {err}")

os.chdir("..")

try:
    os.rmdir("my second folder")
except FileNotFoundError as err:
    print(f"Change to parent directory of 'my second folder'. Error: {err}")