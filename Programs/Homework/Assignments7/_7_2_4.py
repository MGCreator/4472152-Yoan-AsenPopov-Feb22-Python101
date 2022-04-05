import _63
import os
import datetime

class Person:

    def __init__(self, name, todo_list):
        self.name = name
        self.todo_list = todo_list
        print(type(self.todo_list))

    def get_name(self):
        print(f"Name: {self.name}", end=" ")
        return self.name

    def set_name(self, name):
        self.name = name
        return name


def list_as_string(listing):
    strings = ''
    for x in range(len(listing)):
        strings = strings + f"No.{x + 1}:" + listing[x]
        if x + 1 != len(listing):
            strings = strings + ','
        else:
            pass
    return strings


def update_log():
    os.chdir("d:/Infrastucture")
    e = datetime.datetime.now()
    with open('log.txt', 'a') as f:
        if p1_new_name != p1_current_name:
            f.write(f"{e}: {p1.get_name()}\n")
        if p2_new_name != p2_current_name:
            f.write(f"{e}: {p2.get_name()}\n")


p1_tasks = []
p2_tasks = []

p1_list = _63.ToDo(p1_tasks)
_63.commands(p1_list)
p2_list = _63.ToDo(p2_tasks)
_63.commands(p2_list)

p1 = Person('Yo', p1_list)
p2 = Person('Po', p2_list)

p1_current_name = p1.get_name()
p1_new_name = ""
p2_current_name = p2.get_name()
p2_new_name = ""

update_log()

p1_new_name = p1_current_name
p2_new_name = p2_current_name

while True:
    command = input("Command from Person: ")
    if command == "setName":
        person = input("Who: ")
        if person == "p1":
            new_name = input("New name: ")
            p1_new_name = new_name
            p1.set_name(new_name)
            update_log()
            p1_current_name = new_name
        elif person == "p2":
            new_name = input("New name: ")
            p2_new_name = new_name
            p2.set_name(new_name)
            update_log()
            p2_current_name = new_name
        else:
            print("No such person")
    if command == "exit":
        break


string_list_p1 = list_as_string(p1_tasks)
string_list_p2 = list_as_string(p2_tasks)

print(f"Your tasks: {string_list_p1}", end=" ")
p1.get_name()
print(f"\nYour tasks: {string_list_p2}", end=" ")
p2.get_name()



if __name__ == "__main__":
    pass
