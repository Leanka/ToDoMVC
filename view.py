def display_tasks_list(tasks_dict):
    for (index, name) in enumerate(tasks_dict['name']):
        print(index, name, tasks_dict['id'][index])
    # add format + ljust for every single value in 

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

