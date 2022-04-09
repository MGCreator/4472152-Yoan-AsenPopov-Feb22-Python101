from asyncio.windows_events import NULL
from itertools import count
from msilib.schema import Error
import re
import sqlite3
import shutil

columns = shutil.get_terminal_size().columns


def createPersonTable(baza):
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {baza} (id INTEGER, name TEXT, age INTEGER)")


def createToDoTable(baza):
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {baza} (id INTERGER, todo TEXT)")




def Create(baza):
    insert_qry = f"INSERT INTO {baza} VALUES (?, ?, ?);"

    while True:  
        num = checkID(baza)
        if(num != None):
            break
    user_record_name = input("Name: ")
    user_record_age = int(input("Age: "))
    cursor.execute(insert_qry, (num, user_record_name, user_record_age))
    conn.commit()
    return user_record_name


def checkID(baza):
    cursor.execute(f"SELECT * from {baza}")
    results = cursor.fetchall()
    id_number = int(input("ID: "))
    for rec in results:
        if rec[0] == id_number:
            print("This number is occupied. Try new number.")
            return
        if rec==None: 
            break
    return id_number



def Create_todo(*baza):
    insert_qry = f"INSERT INTO {baza[0]} VALUES (?, ?);"
    
    while True:  
        num = checkID(baza[0])
        if(num != None):
            break
    try:
        task_record = baza[1]
    except:
        task_record = input("What task: ")
    cursor.execute(insert_qry, (num, task_record))
    conn.commit()


def getTableLen(baza):
    counter = 0
    cursor.execute(f"SELECT * from {baza}")
    while True: 
        record=cursor.fetchone() 
        if record==None: 
            break
        else:
            counter += 1
    return counter


def Read(*baza):
    cursor.execute(f"SELECT * from {baza[0]}")
    try:
        read_id = baza[1]
    except:
        read_id = int(input("Which person ID: "))
    while True: 
        record=cursor.fetchone() 
        if record==None: 
            print("No such person.")
            break  
        if record[0] == read_id:
            print (record)
            return record


def Read_todo(*baza):
    cursor.execute(f"SELECT * from {baza[0]}")
    try:
        read_id = baza[1]
    except:
        read_id = int(input("Which task ID: "))
    while True: 
        record=cursor.fetchone() 
        if record==None: 
            print("No such task number.")
            break  
        if record[0] == read_id:
            print (record)
            return record


def Update(*baza):
    update_qry_name = f"UPDATE {baza[0]} SET name = ? WHERE id = ?;"
    update_qry_age = f"UPDATE {baza[0]} SET age = ? WHERE id = ?;"

    try:
        new_update = baza[2]
    except:
        new_update = input("What do you want to update (name or age): ")
    if new_update == "name":
        try:
            new_name = baza[1]
            old_name = baza[3]
        except:
            new_name = input("New name: ")
            old_name = input("His/Her old name: ")
        cursor.execute(update_qry_name, (new_name, old_name))
    elif new_update == "age":
        new_age = int(input("New age: "))
        name = input("What is his/her name: ")
        cursor.execute(update_qry_age, (new_age, name))
    conn.commit()


def Update_todo(*baza):
    update_qry_task = f"UPDATE {baza[0]} SET todo = ? WHERE id = ?;"
    try:
        num = baza[1]
    except:
        num = int(input("Which id: "))
    new_task = input("New task: ")
    cursor.execute(update_qry_task, (new_task, num))
    conn.commit()


def Delete(*baza):
    delete_qry = f"DELETE from {baza[0]} where name=?;"

    try:
        del_name = baza[1]
    except:
        del_name = input("Who do you want to delete: ")
    cursor.execute(delete_qry, (del_name,))
    conn.commit()


def Delete_todo(*baza):
    delete_qry = f"DELETE from {baza[0]} where id=?;"

    try:
        del_id = baza[1]
    except:
        del_id = int(input("ID of task to be del: "))
    cursor.execute(delete_qry, (del_id,))
    conn.commit()


def addTestData(baza):
    data = [('George', 16), ('Michael', 17), \
            ('Logan', 20), ('Olga', 23), \
            ('Misha', 27), ('Bobby', 28)]
    cursor.executemany(f"INSERT INTO {baza} VALUES (?, ?)", data)
    conn.commit()


def addTestData_todo(baza):
    data = [(1, 'a'), (2, 'b'), \
            (3, 'c'), (4, 'd'), \
            (5, 'e'), (6, 'f')]
    cursor.executemany(f"INSERT INTO {baza} VALUES (?, ?)", data)
    conn.commit()


def getAllUser(baza):
    cursor.execute(f"SELECT * from {baza}")
    results = cursor.fetchall()
    for rec in results:
        print(rec)

def getAllUser_todo(baza):
    cursor.execute(f"SELECT * from {baza}")
    results = cursor.fetchall()
    for rec in results:
        print(rec)


conn = sqlite3.connect('appDB.db')

cursor = conn.cursor()

createPersonTable("person")

print(getTableLen("person"))




#createToDoTable("todo")
#Create_todo("todo")

# cursor.execute("DROP TABLE person_app")
# conn.commit()
# cursor.execute("DELETE FROM person_app")
# conn.commit()
# cursor.execute("DELETE FROM person_app_todo")
# conn.commit()


#Commands for todo
# while True:
#     conn = sqlite3.connect('appDB.db')

#     cursor = conn.cursor()

#     print("c: Create a user record\
#         r: Read a user record\
#         u: Update a user record\
#         d: Delete a user\
#         t: Add test data\
#         g: Get all users\
#         q: Quit".center(columns))

#     command = input("command:")
#     try:
#         if command == "c":
#             Create_todo("todo")
#         elif command == "r":
#             Read_todo("todo")
#         elif command == "u":
#             Update_todo("todo")
#         elif command == "d":
#             Delete_todo("todo")
#         elif command == "t":
#             addTestData_todo("todo")
#         elif command == "g":
#             getAllUser_todo("todo")
#         elif command == "q":
#             break
#         else:
#             print("Invalid command!")

#         conn.commit()
#         conn.close()
#     except:
#         print("error in operation")
#         conn.rollback()
#         conn.close()



# Commands for person
# while True:
#     conn = sqlite3.connect('appDB.db')

#     cursor = conn.cursor()

#     print("c: Create a user record\
#         r: Read a user record\
#         u: Update a user record\
#         d: Delete a user\
#         t: Add test data\
#         g: Get all users\
#         q: Quit".center(columns))

#     command = input("command:")
#     try:
#         if command == "c":
#             Create("person")
#         elif command == "r":
#             Read("person")
#         elif command == "u":
#             Update("person")
#         elif command == "d":
#             Delete("person")
#         elif command == "t":
#             addTestData("person")
#         elif command == "g":
#             getAllUser("person")
#         elif command == "q":
#             pass
#         else:
#             print("Invalid command!")

#         conn.commit()
#         conn.close()
#     except:
#         print("error in operation")
#         conn.rollback()
#         conn.close()
