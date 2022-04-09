import sqlite3
import shutil

columns = shutil.get_terminal_size().columns

def createPersonTable():
    c.execute("CREATE TABLE person (name TEXT, age INTEGER)")


conn = sqlite3.connect('appDB.db')

insert_qry = "INSERT INTO person name=? age=?"

try:
    c = conn.cursor()
    createPersonTable()

    while True:
        print('''create: Create a user record 
        read: Read a user record
        update: Update a user record
        delete: Delete a user'''.center(columns))
        command = input("command:")
        if command == "create":
            user_record_name = input("Name: ")
            user_record_age = input("Age: ")
            c.execute(insert_qry, user_record_name, user_record_age)

except:
    pass
conn.commit
conn.close