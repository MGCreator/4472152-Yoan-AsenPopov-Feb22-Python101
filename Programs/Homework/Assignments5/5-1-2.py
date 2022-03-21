marks = ['Outstanding', 'Good', 'Unsatisfactory', 'Good', 'Good', 'Poor']
marks2 = []

lists = [marks, marks2]

for item in lists:
    num_of_items = len(item)
    if num_of_items > 0:
        print(f"{item} is not empty")
    else:
        print(f"{item} is empty")

    #Pythonic way / recommended by PEP8
    if not num_of_items:
        print(f"{item} is empty")
    else:
        print(f"{item} is not empty")
