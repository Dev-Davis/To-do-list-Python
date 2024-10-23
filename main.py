todos = []

while True:
    user_action = input("Type add, show, edit, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a task: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'edit':
            number = int(input('Number of item to edit: '))
            number = number - 1
            new_task = input('Enter new task: ')
            todos[number] = new_task
        case 'exit':
            break

print("Bye!")


