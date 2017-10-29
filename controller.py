from model import*

def take_user_input(input_message=' ', max_input_length=1):
    while True:
        users_input = input("{}: ".format(input_message))
        users_input = users_input.strip()
        if (len(users_input) != 0) and (len(users_input) <= max_input_length):
            return users_input

def take_task_index(task_list_length=0):
    while True:
        try:
            task_index = int(take_user_input('Pass tasks number', len(str(task_list_length))))
            task_index -= 1  # Decrement user input by one, prior checking its validation as list index
            if task_index not in range(task_list_length):
                raise IndexError
        except (IndexError, ValueError):
            pass  # add clearing one line above for smooth passing input
        else:
            return task_index

def prepare_task_to_be_viewed():
    pass

def prepare_task_list_to_be_viewed(todo_list):
    tasks_ids_and_names = {'id': [], 'name': []}

    for task in todo_list:
        tasks_ids_and_names['id'].append(str(task.__dict__['is_done']))
        tasks_ids_and_names['name'].append(task.__dict__['name'])

    return tasks_ids_and_names

def main():
    tasks_to_do = TaskList()
    while True:
        # show menu from view module
        chosen_menu_option = take_user_input("Choose an option by it's number")
        
        if len(tasks_to_do.todo_list) == 0:
            # show empty list communicate
        elif chosen_menu_option == "1":  # Display items list
            pass
        elif chosen_menu_option == "2":  # Display specific item's details
            pass
        elif chosen_menu_option == "3":  # Add item
            pass
        elif chosen_menu_option == "4":  # Change items name
            pass
        elif chosen_menu_option == "5":  # Change items desctiption
            pass
        elif chosen_menu_option == "6":  # Mark item as done
            pass
        elif chosen_menu_option == "7":  # Delete item
            pass
        elif chosen_menu_option == "8":  # Exit
            pass

if __name__ == '__main__':
    main()


