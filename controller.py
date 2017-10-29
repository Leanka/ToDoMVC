from model import*
import sys

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

def prepare_task_list_to_be_viewed():
    pass

def check_if_choice_is_workable(chosen_option):
    possible_options_if_no_task_exists = ["3", "8"]

    return chosen_option in possible_options_if_no_task_exists

def main():
    tasks_to_do = TaskList()
    while True:
        # show menu from view module
        chosen_menu_option = take_user_input("Choose an option by it's number")

        if len(tasks_to_do.todo_list) == 0 and check_if_choice_is_workable(choice):
            pass
            # show empty list & bad choice communicate
        elif chosen_menu_option == "1":  # Display items list
            pass
        elif chosen_menu_option == "2":  # Display specific item's details
            pass
        elif chosen_menu_option == "3":  # Add item
            task_name = take_user_input('Pass tasks name (max 20 char)', 20)
            task_description = take_user_input('Pass tasks description (max 150 char)', 150)
            tasks_to_do.add_task(task_name, task_description)

        elif chosen_menu_option == "4":  # Change items name
            pass
        elif chosen_menu_option == "5":  # Change items desctiption
            pass
        elif chosen_menu_option == "6":  # Mark item as done
            chosen_task_index = take_task_index(len(tasks_to_do.todo_list))
            tasks_to_do.todo_list[chosen_task_index].mark_as_done()
            # print task.name task has been done! message

        elif chosen_menu_option == "7":  # Delete item
            chosen_task_index = take_task_index(len(tasks_to_do.todo_list))
            tasks_to_do.remove_task(chosen_task_index)
            # print deleted item message

        elif chosen_menu_option == "8":  # Exit
            # print goodbye message
            sys.exit()

if __name__ == '__main__':
    main()


