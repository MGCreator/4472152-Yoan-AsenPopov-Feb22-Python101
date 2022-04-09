import shutil

class ToDo:

    def __init__(self, list_todo):
        self.list_todo = list_todo

    def adding_task(self, new_task):
        self.list_todo.append(new_task)

    def remove_existing_item(self, remove_task):
        counter = 0
        for item in self.list_todo:
            if item == remove_task:
                self.list_todo.remove(remove_task)
                break
            else:
                counter += 1
            if counter == len(self.list_todo):
                print("No such item")

    def check_item(self, check_item):
        for item in self.list_todo:
            if item == check_item:
                print("It exists")
            else:
                print("It does not exists")

    def print_list(self):
        print(self.list_todo)

    def return_list(self):
        pass

    def exit_list(self):
        print(*self.list_todo, sep = ", ")



columns = shutil.get_terminal_size().columns

def commands(_list_):

    print("add: adding a new task\
        remove: remove task\
        check: check for existing task\
        print: prints the list\
        exit: Exit".center(columns))

    while True:
        command = input("Command: ")
        if command == "add":
            task = input("New task: ")
            _list_.adding_task(task)
        elif command == "remove":
            task = input("Remove a task: ")
            _list_.remove_existing_item(task)
        elif command == "check":
            task = input("Check a task: ")
            _list_.check_item(task)
        elif command == "print":  # print items in the list
            _list_.print_list()
        elif command == "return":  # return to-do list of string
            pass
        elif command == "exit":
            _list_.exit_list()
            break
        else:
            print("No such command")


tasks = []
list1 = ToDo(tasks)

#commands(list1)
