import sqlite3
import DatabaseHelper
import shutil

conn = sqlite3.connect('appDB.db')

cursor = conn.cursor()

columns = shutil.get_terminal_size().columns


DatabaseHelper.createPersonTable("person1")
#DatabaseHelper.addTestData("person1")
DatabaseHelper.createToDoTable("todo1")
#DatabaseHelper.addTestData_todo("todo1")
conn.commit()
conn.close()

while True:
    conn = sqlite3.connect('appDB.db')

    cursor = conn.cursor()

    print("c: Create a user record\
        r: Read a user record\
        u: Update a user record\
        d: Delete a user\
        t: Add test data\
        g: Get all users\
        q: Quit".center(columns))

    command = input("command:")
    try:
        if command == "c":
            DatabaseHelper.Create("person1")
        elif command == "r":
            DatabaseHelper.Read("person1")
        elif command == "u":
            DatabaseHelper.Update("person1")
        elif command == "d":
            DatabaseHelper.Delete("person1")
        elif command == "t":
            DatabaseHelper.addTestData("person1")
        elif command == "g":
            DatabaseHelper.getAllUser("person1")
        elif command == "q":
            break
        else:
            print("Invalid command!")

        conn.commit()
        conn.close()
    except:
        print("error in operation")
        conn.rollback()
        conn.close()
