import _63


class Person:

    def __init__(self, name, todo_list):
        self.name = name
        self.todo_list = todo_list
        print(type(self.todo_list))

    def get_name(self):
        print(f"Name: {self.name}", end=" ")

    def set_name(self, name):
        self.name = name


def list_as_string(listing):
    strings = ''
    for x in range(len(listing)):
        strings = strings + f"No.{x + 1}:" + listing[x]
        if x + 1 != len(listing):
            strings = strings + ','
        else:
            pass
    return strings


p1_tasks = []
p2_tasks = []

p1_list = _63.ToDo(p1_tasks)
_63.commands(p1_list)
p2_list = _63.ToDo(p2_tasks)
_63.commands(p2_list)

p1 = Person('Yo', p1_list)
p2 = Person('Po', p2_list)

string_list_p1 = list_as_string(p1_tasks)
string_list_p2 = list_as_string(p2_tasks)

print(f"Your tasks: {string_list_p1}", end=" ")
p1.get_name()
print(f"\nYour tasks: {string_list_p2}", end=" ")
p2.get_name()

p1.set_name('Yo1')
p2.set_name('Po1')

if __name__ == "__main__":
    pass
