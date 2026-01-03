tasks = []

def menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

while True:
    menu()
    choice = input("Choose: ")

    if choice == "3":
        break
