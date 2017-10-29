def display_tasks_list():
    pass


def display_single_task_info():
    pass


def display_operation_communicate(noun='something', past_participle_varb='done'):
    print("{} has been {} successfully!".format(noun.title(), past_participle_varb.lower()))

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

