1. Describe the Problem

Wants an interactive to do list that adds todos, provides a list of incomplete to dos, provides a list of complete todos and marks all todos as complete. 

2. Design the Class Interface
Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.

class TodoList:
    def __init__(self):
        pass

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        pass
    
    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        pass

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        pass

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        pass

class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        # Parameters:
        #   task: a string representing the task to be done
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False
        pass

    def mark_complete(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        pass
​
3. Create Examples as Tests
Make a list of examples of how the class will behave in different situations.
# EXAMPLE

"""
Given a new todo represented by a string 
We can add todo to the list of todos 
"""

def test_adding_a_todo(): 
    todo_list = TodoList()
    todo1 = Todo("Do some coding", True)
    todo2 = Todo("Go out with some old friends", False)
    todo_list.add(todo1)
    todo_list.add(todo2)
    assert todo_list.todos == [todo1, todo2]

"""
Given a user wants to see all incomplete todos
Return a list of incomplete todos 
"""

def test_to_see_all_incomplete():
    todo_list = TodoList()
    todo1 = Todo("Do some coding", True)
    todo2 = Todo("Go out with some old friends", False)
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.incomplete == todo2

"""
Given a user wants to see all complete todos
Return a list of complete todos 
"""

def test_to_see_all_complete():
    todo_list = TodoList()
    todo1 = Todo("Do some coding", True)
    todo2 = Todo("Go out with some old friends", False)
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.complete == todo1

""" 
Given give_up???? 
""" 

def test_given_up():

"""
Given a new todo 
I can see the new todo 
"""

def test_new_todo_completed():
    todo = Todo("Do some coding")
    assert todo.task == "Do some coding"
    assert todo.is_complete == True

"""
Given a task needs to be done
Return a string representing the task needs to be done 
"""

def test_if_todo_needs_to_be_completed_sets_to_False():
    todo = Todo()
    assert todo == False 

"""
Given a todo is completed
Mark as complete 
"""

def test_if_todo_needs_to_be_marked_complete_sets_to_True():
    todo = Todo() 
    assert todo == True 



