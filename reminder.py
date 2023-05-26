import json
reminder = []
with open('reminder.txt') as f:
    reminder = json.load(f)


def chooseOptions():
    while True:
        options = """
        1. Create
        2. Read
        3. Delete
        4. Sort by priority asc
        5. Search by priority
        6. Quit
        """
        print(options)
        option = input("\nChoose option: ")

        if option == '1':
            create()
        elif option == '2':
            read()
        elif option == '3':
            delete()
        elif option == '4':
            sort()
        elif option == '5':
            search()
        elif option == '6':
            print("Quit")
            break
        else:
            print(f"\nChoose number from 1 to 5!\n")


def create():
    title = input("\nTitle: ")
    content = input("Content: ")
    priority = input("Priority: ")
    remind = {
        'title': title,
        'content': content,
        'priority': priority
    }
    reminder.append(remind)
    save(reminder)

def read():
    sort()
    with open('reminder.txt') as f:
        content = json.load(f)
    for item in content:
        for key, value in dict(item).items():
            print(f"{key}: {value}")
        print("\n")

    

def delete():
    delete = input("\nTitle to delete: ")
    for i, remind in enumerate(reminder.copy()):
        if remind['title'] == delete:
            del reminder[i]
            save(reminder)
            return None
    print(f"{delete} doesn't exist.")


def search():
    prio = input("Enter priority: ")
    for remind in reminder:
        if remind['priority'] == prio:
            print(remind)
            return
    print(f"{prio} doesn't exist")


def save(temp_reminder):
    with open('reminder.txt', 'w') as f:
        f.write(json.dumps(temp_reminder))
        
def sort():
    sorted_list = sorted(reminder, key=lambda x: x['priority'])
    save(sorted_list)



chooseOptions()
