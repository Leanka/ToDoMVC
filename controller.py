
def take_user_input(input_message=' ', max_input_length=1):
    while True:
        users_input = input("{}: ".format(input_message))
        if len(users_input.strip()) == 0:
            # show message from view
        elif len(users_input) > max_input_length:
            # show message from view
        else:
            return users_input            

def take_task_index(task_list_length=0):
    while True:
        try:
            task_index = int(take_user_input('Pass tasks number: ', len(str(task_index))))
            task_index -= 1  # Decrement user input by one, prior checking its validation as list index
            if task_index not in range(task_list_length):
                raise IndexError("Task position out of scope.\n")
        except IndexError as error_message:
            print(error_message)  # show message from view?
        except TypeError as error_message:
            print(error_message)  # show message from view?
        else:
            return task_index

def prepare_task_to_be_viewed():
    pass

def prepare_task_list_to_be_viewed():
    pass

def main():
    pass

if __name__ == '__main__':
    main()

