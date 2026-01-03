tasks = []


def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully")

def view_tasks():
    if not tasks:
        print("No tasks found")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

while True:
    menu()
    choice = input("Choose: ")

    if choice == "1":
        add_task()

    if choice == "2":
        view_tasks()

    if choice == "3":
        break

print(tasks)


