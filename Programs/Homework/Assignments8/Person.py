from asyncio import tasks
from pip import main
import _63
import os
import datetime
import sqlite3
import DatabaseHelper
import shutil
import pandas as pd
import json

columns = shutil.get_terminal_size().columns

class Person:

    def __init__(self, name, todo_list):
        self.name = name
        self.todo_list = todo_list

    def get_name(self):
        return self.name
    
    def get_name_print(self):
        print(f"Name: {self.name}", end=" ")
        return self.name

    def set_name(self, name):
        self.name = name
        return name


def list_as_string(listing):
    strings = ''
    for x in range(len(listing)):
        strings = strings + f"No.{x + 1}: {listing[x]}"
        if x + 1 != len(listing):
            strings = strings + ', '
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


conn = sqlite3.connect('appDB.db')

cursor = conn.cursor()
DatabaseHelper.createPersonTable("person_app")
DatabaseHelper.createToDoTable("person_app_todo")

p1_tasks = []
p2_tasks = []

p1_list = _63.ToDo(p1_tasks)
_63.commands(p1_list)
p2_list = _63.ToDo(p2_tasks)
_63.commands(p2_list)

db_name_p1 = DatabaseHelper.Create("person_app")
DatabaseHelper.Create_todo("person_app_todo", list_as_string(p1_tasks))
p1 = Person(db_name_p1, p1_list)

db_name_p2 = DatabaseHelper.Create("person_app")
DatabaseHelper.Create_todo("person_app_todo", list_as_string(p2_tasks))
p2 = Person(db_name_p2, p2_list)

p1_current_name = p1.get_name()
p1_new_name = ""
p2_current_name = p2.get_name()
p2_new_name = ""

update_log()

p1_new_name = p1_current_name
p2_new_name = p2_current_name


def updatePerson(person):
    new_name = input("New name: ")
    #p1_new_name = new_name
    if person == "p1":
        p1.set_name(new_name)
        id = 1
        DatabaseHelper.Update("person_app", new_name, "name", id)
    else:
        p2.set_name(new_name)
        id = 2
        DatabaseHelper.Update("person_app", new_name, "name", id)
    update_log()
    

def deletePerson(n):
    DatabaseHelper.Delete("person_app", n)


def getPersonData(id):

    person = DatabaseHelper.Read('person_app', id)

    #todo = DatabaseHelper.Read_todo('person_app_todo', id)

    g = [person]
    #g1 = [todo]
    df = pd.DataFrame(g, columns = ['ID','Name','Age'])
    #df1 = pd.DataFrame(g1, columns = ['ID','ToDo'])
    print(df)
    #print(df1)


def getJson(id):
    person = DatabaseHelper.Read('person_app', id)

    todo = DatabaseHelper.Read_todo('person_app_todo', id)

    x = {
    "id": f"{person[0]}",
    "name": f"{person[1]}",
    "age": person[2],
    "todo": f"{todo[1]}"
    }

    y = json.dumps(x, indent=4)

    print(y)


while True:
    try:

        conn = sqlite3.connect('appDB.db')
        cursor = conn.cursor()

        print("\nsetName: set a new name\
            getName: prints current name\
            del: delete a person\
            gData: print current data in fancy way\
            json: print current data in json\
            ctodo: create new todo list\
            rtodo: read todo list\
            utodo: update todo list\
            dtodo: delete todo list\
            q: Exit".center(columns))

        command = input("Command from Person: ")
        if command == "setName":
            person = input("Which object: ")
            if person == "p1" or person == "p2":
                updatePerson(person)
            else:
                print("No such person")

        elif command == "getName":
            person = input("Which object: ")
            if person == "p1":
                p1.get_name_print()
            elif person == "p2":
                p2.get_name_print()
            else:
                print("No such person")

        elif command == "del":
            conn = sqlite3.connect('appDB.db')
            cursor = conn.cursor()
            person = input("Which object: ")
            if person == "p1":
                name_for_del = p1.get_name()
                print(name_for_del)
                deletePerson(name_for_del)
                del p1
            elif person == "p2":
                deletePerson(p2.get_name())
                del p2
            else:
                print("No such person")

        elif command == "gData":
            id = int(input("ID of a person/task: "))
            getPersonData(id)

        elif command == "json":
            id = int(input("ID of a person/task: "))
            getJson(id)

        elif command == "ctodo":
            id = int(input("Choose new ID: "))
            new_task = []
            new_list = _63.ToDo(new_task)
            _63.commands(new_list)
            DatabaseHelper.Create_todo("person_app_todo", list_as_string(new_task), id)

        elif command == "rtodo":
            id = int(input("ID of a task: "))
            DatabaseHelper.Read_todo("person_app_todo", id)

        elif command == "utodo":
            id = int(input("ID of a task: "))
            DatabaseHelper.Update_todo("person_app_todo", id)

        elif command == "dtodo":
            id = int(input("ID of a task: "))
            DatabaseHelper.Delete_todo("person_app_todo", id)

        elif command == "q":
            break

        else:
            print("No such command.")

        conn.commit()
        conn.close()
    except:
        print("error in operation")
        conn.rollback()
        conn.close()


string_list_p1 = list_as_string(p1_tasks)
string_list_p2 = list_as_string(p2_tasks)

try:
    print(f"Your tasks: {string_list_p1}", end=" ")
    p1.get_name_print()
except:
    pass
try:
    print(f"\nYour tasks: {string_list_p2}", end=" ")
    p2.get_name_print()
except:
    pass



if __name__ == "__main__":
    pass
    #main()
