class Todo:
    def __init__(self, task, status):
        self.task = task
        self.status = status

    def mark_complete(self):
        if self.status == "Complete":
            return True 