from lib.pjct_diary_class import *
from lib.pjct_diary_entry_class import *
from lib.pjct_todo_list import *
from lib.pjct_todos import *
from lib.pjct_extract_mobiles import *

def test_add_diary_entries_to_diary():
    diary = Diary()
    diary_entry1 = DiaryEntry("31 July", "Do some coding")
    diary_entry2 = DiaryEntry("1 August", "Go out with some old friends")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.entries == [diary_entry1, diary_entry2]


# """
# Given the word count of all the entries 
# Returns the total word count of the whole contents of the diary 
# """

def test_count_total_words_for_diary():
    diary = Diary()
    diary_entry1 = DiaryEntry("31 July", "Do some coding")
    diary_entry2 = DiaryEntry("1 August", "Go out with some old friends")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary_entry1.count_words() == 3
    assert diary_entry2.count_words() == 6
    assert diary.count_words() == 9


# """
# Given the reading time of all the entries 
# Returns the total reading time for the whole contents of the diary 
# """

def test_add_total_reading_time_for_diary():
    diary = Diary()
    diary_entry1 = DiaryEntry("31 July", "Do some coding")
    diary_entry2 = DiaryEntry("1 August", "Go out with some old friends")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary_entry1.reading_time(200) == 0.015
    assert diary_entry2.reading_time(200) == 0.03
    assert diary.reading_time(200) == 0.045

# """
# Given I add two entries, one long and one short
# And I call #find_best_entry_for_reading_time
# With a wpm and minutes that means I can only read the short one 
# Then #find_best_entry_for_reading_time returns the shorter one 
# """

def test_best_reading_chunk():
    diary = Diary()
    diary_entry1 = DiaryEntry("31 July", "Do some coding")
    diary_entry2 = DiaryEntry("1 August", "Go out with some old friends Tuesday")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.best_chunk(2, 3) == diary_entry1

# """
# Given I add a diary entry
# And I call # find_best
# With a wpm and a minutes that means I can read that entry
# Then #find_best returns that entry 
# """

def test_best_reading_chunk_that_fits():
    diary = Diary()
    diary_entry1 = DiaryEntry("31 July", "Do some coding")
    diary.add(diary_entry1)
    assert diary.best_chunk(2, 3) == diary_entry1

# """
# Given I add a diary entry
# And I call # find_best
# With a wpm and a minutes that means I cannot read that entry
# Then #find_best returns None
# """

def test_no_reading_chunk_suitable():
    diary = Diary()
    diary_entry1 = DiaryEntry("1 August", "Go out with some old friends on Tuesday")
    diary.add(diary_entry1)
    assert diary.best_chunk(2, 3) == None

# """
# Given I add two entries
# And I call #find_best_entry_for_reading_time
# With a wpm and minutes that means I can read both 
# Then #find_best_entry_for_reading_time returns the longer one 
# """

def test_best_reading_chunk_for_both():
    diary = Diary()
    diary_entry1 = DiaryEntry("31 July", "Do some coding")
    diary_entry2 = DiaryEntry("1 August", "Go out with some old friends Tuesday")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.best_chunk(2, 4) == diary_entry2

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

# """
# Given a user wants to see all incomplete todos
# Return a list of incomplete todos 
# """

def test_to_see_all_incomplete():
    todo_list = TodoList()
    todo1 = Todo("Do some coding", "Incomplete")
    todo2 = Todo("Go out with some old friends", "Complete")
    todo_list.add(todo1)
    todo_list.add(todo2)
    incomplete_todos = todo_list.incomplete()
    assert todo1 in incomplete_todos

# """
# Given a user wants to see all complete todos 
# Return a list of complete todos 
# """

def test_to_see_if_complete():
    todo_list = TodoList()
    todo1 = Todo("Do some coding", "Incomplete")
    todo2 = Todo("Go out with some old friends", "Complete")
    todo_list.add(todo1)
    todo_list.add(todo2)
    complete_todos = todo_list.complete()
    assert todo2 in complete_todos 


"""
Given we add a todo to diary
We see a list of todos in diary
"""
def test_adding_a_todo_to_diary_to_see_todo_list():
    diary = Diary()
    todo1 = ("Do some coding", "Incomplete")
    diary.add_todo(todo1)
    assert diary.todos == [todo1] 

"""
Given we want to see all  tasks in diary
We return a list of tasks 
"""

def test_see_complete_todos_in_diary():
    diary = Diary()
    todo1 = Todo("Do some coding", "Incomplete")
    todo2 = Todo("Go out with some old friends", "Complete")
    diary.add_todo(todo1)
    diary.add_todo(todo2)
    assert diary.view_all_todos() == [todo1, todo2]

"""
Given we want to all incomplete tasks in diary
We return a list of incomplete tasks 
"""

def test_to_see_list_of_all_incomplete_todos():
    diary = Diary()
    todo1 = Todo("Task 1", "Complete")
    todo2 = Todo("Task 2", "Incomplete")
    todo3 = Todo("Task 3", "Incomplete")
    todo4 = Todo("Task 4", "Complete")
    diary.add_todo(todo1)
    diary.add_todo(todo2)
    diary.add_todo(todo3)
    diary.add_todo(todo4)
    incomplete_todos = diary.incomplete_todos()
    assert len(incomplete_todos) == 2
    assert todo2 in incomplete_todos
    assert todo3 in incomplete_todos


""" 
Given we want all complete tasks in diary
We return a list of incomplete tasks 
"""
def test_to_see_list_of_all_complete_todos():
    diary = Diary()
    todo1 = Todo("Task 1", "Complete")
    todo2 = Todo("Task 2", "Incomplete")
    todo3 = Todo("Task 3", "Incomplete")
    todo4 = Todo("Task 4", "Complete")
    diary.add_todo(todo1)
    diary.add_todo(todo2)
    diary.add_todo(todo3)
    diary.add_todo(todo4)
    complete_todos = diary.complete_todos()
    assert len(complete_todos) == 2
    assert todo1 in complete_todos
    assert todo4 in complete_todos

"""
Given a diary_entry has a mobile number in it
Extract the mobile number
""" 


def test_extracting_a_mobile_number_from_diary_entry():
    mobile_list = MobileList()

    diary_entry_text = "Tessa Cowan's mobile number is 07701099227, and John Doe's mobile is 07987654320."
    diary_entry = DiaryEntry("Tessa Cowan", diary_entry_text)
    extracted_mobiles = diary_entry.extract_mobile()

    if extracted_mobiles:  # Check if the list is not empty before iterating
        for mobile_number in extracted_mobiles:
            mobile_list.add_mobile(mobile_number)

    assert mobile_list.mobile_numbers == ["07701099227", "07987654320"]

