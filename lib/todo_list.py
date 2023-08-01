class TodoList:
    def __init__(self):
        self.todos = []

    def add(self, todo):
        self.todos.append(todo)
    
    def incomplete(self):
        incomplete_todos = []
        for todo in self.todos: 
            if todo.status == "Incomplete":
                incomplete_todos.append(todo)
        return incomplete_todos

    def complete(self):
        complete_todos = []
        for todo in self.todos:
            if todo.status == "Complete":
                complete_todos.append(todo)
        return complete_todos 

    def give_up(self):
        self.status = "Complete"