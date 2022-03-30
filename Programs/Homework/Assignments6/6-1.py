class Person:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        print(f"Name: {self.name}")

    def set_name(self, name):
        self.name = name


p1 = Person('Yo')
p2 = Person('Po')

p1.get_name()
p2.get_name()

p1.set_name('Yo1')
p2.set_name('Po1')

p1.get_name()
p2.get_name()
