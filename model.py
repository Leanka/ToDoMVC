
class Task():
    
    def __init__(self, name, description):
        if isinstance(name, str) and isinstance(description, str):
            self.name = name
            self.description = description
            self.is_done = False

    def mark_as_done(self):
        self.is_done = True

    def mark_as_undone(self):
        self.is_done = False

    def change_name(self, new_name):
        self.name = new_name

    def change_description(self, new_description):
        self.description = new_description


class TaskList():
    
    def __init__(self):
        self.todo_list = []

    def add_task(self, name, description):
        self.todo_list.append(Task(name, description))

    def remove_task(self, task_index):
        if isinstance(task_index, int):
            del self.todo_list[task_index]


# example_task = Task('idź spać', 'no wstań i idź')
# sec_task = Task('skończ waść', 'wstydu oszczędź')
# print(example_task.__dict__)
todo = TaskList()
todo.add_task('coś', 'cokolwiek byle było')
todo.add_task('idź spać', 'no wstań i idź')
todo.add_task('skończ waść', 'wstydu oszczędź')

