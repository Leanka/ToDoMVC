
class Task():
    pass

class TaskList():
    
    def __init__(self):
        self.todo_list = []

    def add_task(self, name, description):
        self.todo_list.append(Task(name, description))

    def remove_task(self, task_index):
        if isinstance(task_index, int):
            del self.todo_list[task_index]

    

