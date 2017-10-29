from model import*
from view import*
import sys


def take_user_input(input_message=' ', max_input_length=1):
    while True:
        users_input = input("{}: ".format(input_message))
        users_input = users_input.strip()
        if (len(users_input) != 0) and (len(users_input) <= max_input_length):
            return users_input

def take_task_index(task_list_length):
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

def prepare_single_task_to_be_viewed(task):
    objects_dict = task.__dict__
    max_line_len = 50
    task_info = []

    for attribute in objects_dict:
        if len(attribute + str(objects_dict.get(attribute))) > 50:
            string_set_to_max_length = "{:150}".format(objects_dict.get(attribute))
            sliced_string = string_set_to_max_length[:50] + '\n'
            sliced_string += string_set_to_max_length[50:100] + '\n'
            sliced_string += string_set_to_max_length[100:]
            sliced_string = sliced_string.strip()

            title_bar = "{:^50}".format(attribute)

            task_info.append(title_bar)
            task_info.append(sliced_string)
        else:
            task_info.append("{:^25}:{:^25}".format(attribute, objects_dict.get(attribute)))

    return task_info


def prepare_tasks_to_be_viewed(todo_list):
    tasks_names = []
    tasks_status = []
    attributes_values_sorted_in_lists = []

    for task in todo_list:
        tasks_names.append(task.__dict__['name'])
        if task.__dict__['is_done']:
            tasks_status.append('DONE')
        else:
            tasks_status.append('NOT DONE')
    
    attributes_values_sorted_in_lists.append(tasks_status)
    attributes_values_sorted_in_lists.append(tasks_names)

    return attributes_values_sorted_in_lists


def check_if_choice_is_workable(chosen_option):
    possible_options_if_no_task_exists = ["3", "8"]

    return chosen_option in possible_options_if_no_task_exists


def main():
    tasks_to_do = TaskList()
    while True:
        display_main_menu()
        chosen_menu_option = take_user_input("Choose an option by it's number")

        if len(tasks_to_do.todo_list) == 0 and check_if_choice_is_workable(choice):
            display_operation_communicate('Invalid choice', 'made', 'No tasks to work on. Try to add some.')

        elif chosen_menu_option == "1":  # Display items list
            display_tasks_list(prepare_tasks_to_be_viewed(tasks_to_do.todo_list))

        elif chosen_menu_option == "2":  # Display specific item's details
            chosen_task_index = take_task_index(len(tasks_to_do.todo_list))
            tasks_info = prepare_single_task_to_be_viewed(tasks_to_do.todo_list[chosen_task_index])
            display_single_task_info(tasks_info)

        elif chosen_menu_option == "3":  # Add item
            task_name = take_user_input('Pass tasks name (max 20 char)', 20)
            task_description = take_user_input('Pass tasks description (max 150 char)', 150)
            tasks_to_do.add_task(task_name, task_description)
            display_operation_communicate('task', 'added')

        elif chosen_menu_option == "4":  # Change items name
            chosen_task_index = take_task_index(len(tasks_to_do.todo_list))
            tasks_new_name = take_user_input('Pass tasks name (max 20 char)', 20)
            tasks_to_do.todo_list[chosen_task_index].change_name(tasks_new_name)
            display_operation_communicate('name', 'changed')

        elif chosen_menu_option == "5":  # Change items desctiption
            chosen_task_index = take_task_index(len(tasks_to_do.todo_list))
            tasks_new_description = take_user_input('Pass tasks description (max 150 char)', 150)
            tasks_to_do.todo_list[chosen_task_index].change_description(tasks_new_description)
            display_operation_communicate('description', 'changed')

        elif chosen_menu_option == "6":  # Mark item as done
            chosen_task_index = take_task_index(len(tasks_to_do.todo_list))
            tasks_to_do.todo_list[chosen_task_index].mark_as_done()
            display_operation_communicate('task', 'marked')

        elif chosen_menu_option == "7":  # Delete item
            chosen_task_index = take_task_index(len(tasks_to_do.todo_list))
            tasks_to_do.remove_task(chosen_task_index)
            display_operation_communicate('task', 'deleted')

        elif chosen_menu_option == "8":  # Exit
            display_operation_communicate('program', 'closed')
            sys.exit()

if __name__ == '__main__':
    main()


