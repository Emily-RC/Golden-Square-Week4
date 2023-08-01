from lib.todo import *
from lib.todo_list import *

"""
Given a new todo represented by a string 
We can add todo to the list of todos 
"""

def test_adding_a_todo(): 
    todo_list = TodoList()
    todo1 = Todo("Do some coding", "Incomplete")
    todo2 = Todo("Go out with some old friends", "Complete")
    todo_list.add(todo1)
    todo_list.add(todo2)
    assert todo_list.todos == [todo1, todo2]

"""
Given a user wants to see all incomplete todos
Return a list of incomplete todos 
"""

def test_to_see_all_incomplete():
    todo_list = TodoList()
    todo1 = Todo("Do some coding", "Incomplete")
    todo2 = Todo("Go out with some old friends", "Complete")
    todo_list.add(todo1)
    todo_list.add(todo2)
    incomplete_todos = todo_list.incomplete()
    assert todo1 in incomplete_todos

"""
Given a user wants to see all complete todos 
Return a list of complete todos 
"""

def test_to_see_if_complete():
    todo_list = TodoList()
    todo1 = Todo("Do some coding", "Incomplete")
    todo2 = Todo("Go out with some old friends", "Complete")
    todo_list.add(todo1)
    todo_list.add(todo2)
    complete_todos = todo_list.complete()
    assert todo2 in complete_todos 

"""
Given all todos are complete
Mark all todos as complete 
"""

def test_give_up_and_mark_all_tasks_as_complete():
    todo_list = TodoList()
    todo1 = Todo("Do some coding", "Complete")
    todo2 = Todo("Go out with some old friends", "Complete")
    todo_list.add(todo1)
    todo_list.add(todo2)
    assert todo1 in todo_list.todos
    assert todo2 in todo_list.todos 
    todo_list.give_up() 
    assert todo1.status == "Complete"
    assert todo2.status == "Complete"