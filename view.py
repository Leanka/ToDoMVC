import time
import sys


def display_tasks_list(tasks_attributes_lists):
    first_column_title = ''
    second_column_title = 'id'
    third_column_title = 'name'

    id_list_index = 0
    name_list_index = 1

    title_bar = "|{:^3}|{:^10}|{:^20}|".format(first_column_title, second_column_title, third_column_title)
    separator = '-'*len(title_bar)

    print(separator)
    print(title_bar)
    print(separator)

    for index in range(len(tasks_attributes_lists[id_list_index])):
        print("|{:^3}|{:^10}|{:>20}|".format(index+1, 
                                            tasks_attributes_lists[id_list_index][index], 
                                            tasks_attributes_lists[name_list_index][index]))
        print(separator)
    print('\n')


def display_single_task_info(task_info):
    max_line_len = 50
    separator = '-'*max_line_len

    print(separator)
    for info in task_info:
        print(info)
        print(separator)
    print('\n')

def display_operation_communicate(noun='something', past_participle_varb='done', instructions=''):
    print("{} has been {}! {}".format(noun.title(), past_participle_varb.lower(), instructions))
    time.sleep(2)

def display_main_menu():
    menu = ["Possible oparations:",
            " 1. Display items list",
            " 2. Display specific item's details",
            " 3. Add item",
            " 4. Change items name",
            " 5. Change items desctiption",
            " 6. Mark item as done",
            " 7. Delete item",
            " 8. Exit"]

    for operation in menu:
        print(operation)

