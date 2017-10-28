
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
    pass

