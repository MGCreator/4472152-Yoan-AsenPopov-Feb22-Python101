class ToDo:

    def __init__(self, list_todo):
        self.list_todo = list_todo

    def adding_task(self, new_task):
        self.list_todo.append(new_task)

    def remove_existing_item(self, remove_task):

        for item in self.list_todo:
            if item == remove_task:
                self.list_todo.remove(remove_task)
            else:
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


tasks = []
list1 = ToDo(tasks)
while True:
    command = input("Command: ")
    if command == "add":
        task = input("New task: ")
        list1.adding_task(task)
    elif command == "remove":
        task = input("Remove a task: ")
        list1.remove_existing_item(task)
    elif command == "check":
        task = input("Check a task: ")
        list1.check_item(task)
    elif command == "print":  # print items in the list
        list1.print_list()
    elif command == "return":  # return to-do list of string
        pass
    else:
        print("No such command")
