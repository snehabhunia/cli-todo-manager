tasks = []

def menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

while True:
    menu()
    choice = input("Choose: ")

    if choice == "1":
        add_task()
    
    if choice == "3":
        break

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully")
