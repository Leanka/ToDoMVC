def display_tasks_list(tasks_dict):
    title_bar = "|{:^3}|{:^5}|{:^20}|".format('', 'id', 'name')
    separator = '-'*len(title_bar)

    print(separator)
    print(title_bar)
    print(separator)
    for index in range(len(tasks_dict['name'])):
        print("|{:^3}|{:>5}|{:>20}|".format(index+1, tasks_dict['id'][index], tasks_dict['name'][index]))
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


