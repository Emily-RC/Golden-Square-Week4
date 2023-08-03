class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, todo, status):
        self.task = todo
        self.status = status

    def mark_complete(self):
        if self.status == "Complete":
            return True