from model import*
from view import*
import sys
import os


def take_user_input(input_message=' ', max_input_length=1):
    while True:
        users_input = input("{}: ".format(input_message))
        users_input = users_input.strip()
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        if (len(users_input) != 0) and (len(users_input) <= max_input_length):
            os.system('clear')
            return users_input



def take_task_index(task_list_length):
    while True:
        try:
            task_index = int(take_user_input('Pass tasks number', len(str(task_list_length))))
            task_index -= 1  # Decrement user input by one, prior checking its validation as list index
            if task_index not in range(task_list_length):
                raise IndexError
        except (IndexError, ValueError):
            sys.stdout.write("\033[K")
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


def check_if_choice_is_not_workable(chosen_option):
    possible_options_if_no_task_exists = ["3", "8"]

    return chosen_option not in possible_options_if_no_task_exists


def main():
    os.system('clear')
    tasks_to_do = TaskList()
    max_task_name_length = 20
    max_task_description_length = 150
    while True:
        os.system('clear')
        display_main_menu()
        chosen_menu_option = take_user_input("Choose an option by it's number")
        os.system('clear')

        if (len(tasks_to_do.todo_list) == 0) and check_if_choice_is_not_workable(chosen_menu_option):
            if chosen_menu_option in ('1', '2', '3', '4', '5', '6', '7', '8'):
                display_operation_communicate('Invalid choice', 'made', 'No tasks to work on. Try to add some.')
                input('\n Press any key to continue.')
                
        elif chosen_menu_option == "1":  # Display items list
            display_tasks_list(prepare_tasks_to_be_viewed(tasks_to_do.todo_list))
            input('\n Press any key to continue.')

        elif chosen_menu_option == "2":  # Display specific item's details
            display_tasks_list(prepare_tasks_to_be_viewed(tasks_to_do.todo_list))
            chosen_task_index = take_task_index(len(tasks_to_do.todo_list))
            tasks_info = prepare_single_task_to_be_viewed(tasks_to_do.todo_list[chosen_task_index])
            display_single_task_info(tasks_info)
            input('\n Press any key to continue.')

        elif chosen_menu_option == "3":  # Add item
            task_name = take_user_input('Pass new tasks name (max 20 char)', max_task_name_length)
            task_description = take_user_input('Pass new tasks description (max 150 char)', max_task_description_length)
            tasks_to_do.add_task(task_name, task_description)
            display_tasks_list(prepare_tasks_to_be_viewed(tasks_to_do.todo_list))
            display_operation_communicate('task', 'added')
            input('\n Press any key to continue.')

        elif chosen_menu_option == "4":  # Change items name
            display_tasks_list(prepare_tasks_to_be_viewed(tasks_to_do.todo_list))
            chosen_task_index = take_task_index(len(tasks_to_do.todo_list))
            tasks_new_name = take_user_input('Pass tasks new name (max 20 char)', max_task_name_length)
            tasks_to_do.todo_list[chosen_task_index].change_name(tasks_new_name)
            display_tasks_list(prepare_tasks_to_be_viewed(tasks_to_do.todo_list))
            display_operation_communicate('name', 'changed')
            input('\n Press any key to continue.')

        elif chosen_menu_option == "5":  # Change items desctiption
            display_tasks_list(prepare_tasks_to_be_viewed(tasks_to_do.todo_list))
            chosen_task_index = take_task_index(len(tasks_to_do.todo_list))
            tasks_new_description = take_user_input('Pass tasks new description (max 150 char)', max_task_description_length)
            tasks_to_do.todo_list[chosen_task_index].change_description(tasks_new_description)
            display_tasks_list(prepare_tasks_to_be_viewed(tasks_to_do.todo_list))
            display_operation_communicate('description', 'changed')
            input('\n Press any key to continue.')

        elif chosen_menu_option == "6":  # Mark item as done
            display_tasks_list(prepare_tasks_to_be_viewed(tasks_to_do.todo_list))
            chosen_task_index = take_task_index(len(tasks_to_do.todo_list))
            tasks_to_do.todo_list[chosen_task_index].mark_as_done()
            display_tasks_list(prepare_tasks_to_be_viewed(tasks_to_do.todo_list))
            display_operation_communicate('task', 'marked')
            input('\n Press any key to continue.')

        elif chosen_menu_option == "7":  # Delete item
            display_tasks_list(prepare_tasks_to_be_viewed(tasks_to_do.todo_list))
            chosen_task_index = take_task_index(len(tasks_to_do.todo_list))
            tasks_to_do.remove_task(chosen_task_index)
            display_tasks_list(prepare_tasks_to_be_viewed(tasks_to_do.todo_list))
            display_operation_communicate('task', 'deleted')
            input('\n Press any key to continue.')

        elif chosen_menu_option == "8":  # Exit
            display_operation_communicate('program', 'closed')
            sys.exit()

if __name__ == '__main__':
    main()

