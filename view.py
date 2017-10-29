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

    # ValueError: Invalid format specifier if trying to use vars inside format brackets

def display_single_task_info(objects_dict):
    for attribute in objects_dict:
        print(attribute, "=>", objects_dict.get(attribute))
    # add format
    # add pprint


def display_operation_communicate(noun='something', past_participle_varb='done', instructions=''):
    print("{} has been {}! {}".format(noun.title(), past_participle_varb.lower(), instructions))

def display_main_menu():
    menu = [" 1. Display items list",
            " 2. Display specific item's details",
            " 3. Add item",
            " 4. Change items name",
            " 5. Change items desctiption",
            " 6. Mark item as done",
            " 7. Delete item",
            " 8. Exit"]

    for operation in menu:
        print(operation)

