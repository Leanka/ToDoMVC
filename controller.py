
def take_user_input(input_message, max_input_length=1):
    while True:
        users_input = input("{}: ".format(input_message))
        if len(users_input.strip()) == 0:
            # show message from view
        elif len(users_input) > max_input_length:
            # show message from view
        else:
            return users_input            

def take_task_index():
    pass

def prepare_task_to_be_viewed():
    pass

def prepare_task_list_to_be_viewed():
    pass

def main():
    pass

if __name__ == '__main__':
    main()

