class TodoList:
    def __init__(self):
        self.todos = []
        self.todo_complete = []
        # self.todo_incomplete = []

    def add(self, todo):
        self.todos.append(todo)
    
    def incomplete(self):
        incomplete_todos = []
        for todo in self.todos:
            if todo.status == "Incomplete":
                incomplete_todos.append(todo)
        return incomplete_todos

    def complete(self):
        complete_todo = []
        for todo in self.todos:
            if todo.status == "Complete":
                complete_todo.append(todo)
        return complete_todo