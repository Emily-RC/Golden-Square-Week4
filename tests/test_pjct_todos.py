from lib.pjct_todos import *

# """
# Given a new todo task 
# I can see the new task 
# """

def test_new_task():
    todo = Todo("Do some coding", "Incomplete")
    assert todo.task == "Do some coding"
    assert todo.status == "Incomplete"

# """
# Given a todo is complete 
# Mark it as complete 
# """

def test_to_mark_complete_if_completed():
    todo = Todo("Go out with some old friends", "Complete")
    assert todo.task == "Go out with some old friends"
    assert todo.status == "Complete"
