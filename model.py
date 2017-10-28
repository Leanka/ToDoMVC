
class Task():
    
    def __init__(self, name, description):
        if isinstance(name, str) and isinstance(description, str):
            self.name = name
            self.description = description
            self.is_done = False

    def mark_as_done(self):
        self.is_done = True

    def mark_as_undone(self):
        pass

    def change_name(self):
        pass

    def change_description(self):
        pass

class TaskList():
    pass

