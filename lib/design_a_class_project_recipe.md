{{PROBLEM}} Multi-Class Planned Design Recipe
1. Describe the Problem

One: 
    As a user
    So that I can record my experiences
    I want to keep a regular diary

Two: 
    As a user
    So that I can reflect on my experiences
    I want to read my past diary entries

Three:
    As a user
    So that I can reflect on my experiences in my busy day
    I want to select diary entries to read based on how much time I have and my reading speed

Four:
    As a user
    So that I can keep track of my tasks
    I want to keep a todo list along with my diary

Five:
    As a user
    So that I can keep track of my contacts
    I want to see a list of all of the mobile phone numbers in all my diary entries

2. Design the Class System
Consider diagramming out the classes and their relationships. Take care to focus on the details you see as important, not everything. The diagram below uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com

# Nouns 
diary 
diary entry
task
list of tasks 
contact
list of contacts 

# Verbs 
add 
see list of previous diary entries
marking something complete 
read previous entries 
see list of todos 
see list of mobile numbers 


┌────────────────────────────┐
│ Diary                      │
│                            │
│ - add(diary_entry)         │
│ - view_all                 |
| - count_words              |
| - reading_time│            |                     
│ - best_chunk(wpm, mins)    │                                   
│   => [entries...]          │                                   
└───────────┬────────────────┘                                  
            │              |                                      
            │              |                                     
            ▼              |_______________                    ____________________    
┌─────────────────────────┐<_______________|_________________>|Extract Mobile List |
│ DiaryEntry(title, contents)│   __________▼______________    |                    |
│                         │     |TodoList                 |   | - mobile number    |
│ - title                 │     | - add(todo)             |   |____________________|
│ - contents              │     | - view all complete     |             
│ - contact_list          |     | - view all incomplete   |             
| - count_words_for_entry |     |     => [todos]          |        
| - reading_time(wpm)     |     |_________________________|    └─────────────────────────┘         |                           
                                    |
                                    |
                                 __ ▼______________________
                                |Todos                     |
                                | - init(task, status)     |
                                | - mark complete          |
                                |__________________________|




Also design the interface of each class in more detail.

class Diary:
    # User facing properties:
        # Diary entries (list of instances of diary entries )
        # Todos (list of instances of todos)
        # Mobile numbers (list of instances of mobile numbers)

    def __init__(self):
        pass 

    def add(self, diary_entry):
        # Parameters:
        #   diary_entry: an instance of diary entry 
        # Side-effects:
        #   Adds the diary entry to the diary property of the self object
        pass # No code here yet

    def view_all_entries(self):
        # Parameters:
        #   None
        # Returns:
        #   A list of the diary_entry objects 
        pass # No code here yet

    def count_words(self):
        # Parameters:
        #   None
        # Returns:
        #   Word count for all diary entries in total 
        pass # No code here yet

    def reading_time(self, wpm):
        # Parameters:
        #   wpm - words per minute user can read in int type
        # Returns:
        #   reading_time for all diary entries in total 
        pass # No code here yet

    def best_chunk(self, wpm, mins):
        # Parameters:
        #   wpm - words per minute user can read in int type
        #   mins - minutes user has available to read 
        # Returns:
        #   the best reading chunk for a user to read given wpm and mins 
        pass # No code here yet


class DiaryEntry:
    # User-facing properties:
    #   title: string
    #   contents: string

    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string
        # Side-effects:
        #   Sets the title and contents properties
        pass # No code here yet

    def format(self):
        # Returns:
        #   A string of the form "TITLE: CONTENTS"
        pass # No code here yet

    def count_words(self):
        # Parameters:
        #   None
        # Returns:
        #   Word count for diary entry 
        pass # No code here yet

    def reading_time(self, wpm):
        # Parameters:
        #   wpm - words per minute user can read in int type
        # Returns:
        #   reading_time for dary entry  
        pass # No code here yet

    def reading_chunk(self, wpm, mins):
        # Parameters:
        #   wpm - words per minute user can read in int type
        #   mins - minutes user has available to read - int
        # Returns:
        #   a reading chunk string of a diary entry that the reader can read in the given minutes  
        pass # No code here yet

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

class MobileList:
    # User facing propeties:
        # mobile number which is a string 
    
    def __init__(self, mobile_number):
        # Parameters:
            # None 
        # Side effects:
            # Sets the mobile property 
    
   ( def format_mobile_number(self): 
        # Parameters:
            # None 
        # Return:
            # Mobile number in correct format: 00000 000 000 )


3. Create Examples as Integration Tests
Create examples of the classes being used together in different situations and combinations that reflect the ways in which the system will be used.

# EXAMPLE

Class Diary():
""" 
Given all diary entries are added to the diary
We see all diary entries returns in a list 

whole_diary = Diary()
diary_entry1 = DiaryEntry("31 July", "Do some coding")
diary_entry2 = DiaryEntry("1 August", "Go out with some old friends")
whole_diary.add(diary_entry1)
whole_diary.add(diary_entry2)
whole_diary.entries => [diary_entry1, diary_entry2]

""" 
Given adding a new diary entry 
We can add diary entry to diary 
"""

def test_adding_an_entry(): 
    whole_diary = Diary()
    diary_entry1 = DiaryEntry("31 July", "Do some coding")
    diary_entry2 = DiaryEntry("1 August", "Go out with some old friends")
    whole_diary.add(diary_entry1)
    whole_diary.add(diary_entry2)
    assert whole_diary.entries == [diary_entry1, diary_entry2]


"""
Given the word count of all the entries 
Returns the total word count of the whole contents of the diary 
"""

def test_count_total_words_for_whole_diary():
    whole_diary = Diary()
    diary_entry1 = DiaryEntry("31 July", "Do some coding")
    diary_entry2 = DiaryEntry("1 August", "Go out with some old friends")
    whole_diary.add(diary_entry1)
    whole_diary.add(diary_entry2)
    assert diary_entry1.count_words() == 3
    assert diary_entry2.count_words() == 6
    assert whole_diary.count_words() == 9


"""
Given the reading time of all the entries 
Returns the total reading time for the whole contents of the diary 
"""
def test_add_total_reading_time_for_whole_diary():
    whole_diary = Diary()
    diary_entry1 = DiaryEntry("31 July", "Do some coding")
    diary_entry2 = DiaryEntry("1 August", "Go out with some old friends")
    whole_diary.add(diary_entry1)
    whole_diary.add(diary_entry2)
    assert diary_entry1.reading_time(200) == 0.015
    assert diary_entry2.reading_time(200) == 0.03
    assert whole_diary.reading_time(200) == 0.045

"""
Given I add two entries, one long and one short
And I call #find_best_entry_for_reading_time
With a wpm and minutes that means I can only read the short one 
Then #find_best_entry_for_reading_time returns the shorter one 
"""

# def test_best_reading_chunk():
#     whole_diary = Diary()
#     diary_entry1 = DiaryEntry("31 July", "Do some coding")
#     diary_entry2 = DiaryEntry("1 August", "Go out with some old friends Tuesday")
#     whole_diary.add(diary_entry1)
#     whole_diary.add(diary_entry2)
#     assert whole_diary.find_best_entry_for_reading_time(2, 4) == diary_entry1

"""
Given I add a diary entry
And I call # find_best
With a wpm and a minutes that means I can read that entry
Then #find_best returns that entry 
"""

def test_best_reading_chunk_that_fits():
    whole_diary = Diary()
    diary_entry1 = DiaryEntry("31 July", "Do some coding")
    whole_diary.add(diary_entry1)
    assert whole_diary.find_best_entry_for_reading_time(2, 3) == diary_entry1

"""
Given I add a diary entry
And I call # find_best
With a wpm and a minutes that means I cannot read that entry
Then #find_best returns None
"""

def test_no_reading_chunk_suitable():
    whole_diary = Diary()
    diary_entry1 = DiaryEntry("1 August", "Go out with some old friends on Tuesday")
    whole_diary.add(diary_entry1)
    assert whole_diary.find_best_entry_for_reading_time(2, 3) == None

"""
Given I add two entries
And I call #find_best_entry_for_reading_time
With a wpm and minutes that means I can read both 
Then #find_best_entry_for_reading_time returns the longer one 
"""

def test_best_reading_chunk_for_both():
    whole_diary = Diary()
    diary_entry1 = DiaryEntry("31 July", "Do some coding")
    diary_entry2 = DiaryEntry("1 August", "Go out with some old friends Tuesday")
    whole_diary.add(diary_entry1)
    whole_diary.add(diary_entry2)
    assert whole_diary.find_best_entry_for_reading_time(2, 4) == diary_entry2

"""
Given a diary
When we add diary entries 
We see those entries reflected in the diary
"""
diary = Diary()
diary_entry_1 = DiaryEntry("Carte Blanche", "Veracocha")
diary_entry2 = DiaryEntry("Synaesthesia", "The Thrillseekers")
diary.add(diary_entry1)
diary.add(diary_entry2)
diary.diary_entry # => [diary_entry1, diary_entry2]

"""
Given we add a todo to diary
We see a list of todos in diary
"""
diary = Diary()
todo1 = ("Do some coding", "Incomplete")
diary.add(todo1)
diary.todo # => [todo1]

"""
Given we want to see all complete tasks in diary
We return a list of complete tasks 
"""

"""
Given we want to all incomplete tasks in duary
We return a list of incomplete tasks 
"""

class ExtractMobile:

"""
Given a diary_entry has a mobile number in it
Extract the mobile number
""" 

def test_extracting_a_mobile_number_from_diary_entry(): 
    diary_entry = DiaryEntry("Tessa Cowan", "07701099227")
    extracted_mobile = diary_entry.extract_mobile()
    assert extracted_mobile => "07701099227"


class TodoList:

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


4. Create Examples as Unit Tests
Create examples, where appropriate, of the behaviour of each relevant class at a more granular level of detail.

class DiaryEntry:
"""
Given a new entry
I can see the new entry 
"""

def test_new_entry():
    diary_entry = DiaryEntry("31 July", "Do some coding")
    assert diary_entry.title == "31 July"
    assert diary_entry.contents == "Do some coding"

"""
Given a new entry
I can see the word count of the diary entry 
"""

def test_diary_entry_word_count():
    diary_entry = DiaryEntry("31 July", "Do some coding")
    assert diary_entry.count_words() == 3

"""
Given the length of the entry and the reader's wpm 
Returns an estimate of the reading time in minutes for the contents at the given wpm
"""

def test_reading_time_for_diary_entry():
    diary_entry = DiaryEntry("31 July", "Do some coding")
    assert diary_entry.reading_time(200) == 0.015

"""
Given the wpm a read can read and the time that takes per entry
Returns a string repping a chunk of the contents the reader can read in the given minutes 
"""
def test_reading_chunk():
    diary_entry = DiaryEntry("31 July", "Do some coding")
    text = "Do some coding"
    assert diary_entry.reading_chunk(200, 0.015) == text

class Todo:
"""
Given a new todo task 
I can see the new task 
"""

def test_new_task():
    todo = Todo("Do some coding", "Incomplete")
    assert todo.task == "Do some coding"
    assert todo.status == "Incomplete"

"""
Given a todo is complete 
Mark it as complete 
"""

def test_to_mark_complete_if_completed():
    todo = Todo("Go out with some old friends", "Complete")
    assert todo.task == "Go out with some old friends"
    assert todo.status == "Complete"

class TodoList: 

"""
Given a new todo
Add to todo list 
"""

def test_add_new_todo_to_todo_list():
    

class ExtractMobile:

""" 
Given a diary entry has a mobile number in it 
Extract the mobile and append it to a list of mobile numbers 
""" 

def test_extract_mobile_numbers(): 
    diary_entry = DiaryEntry("Tessa Cowan", "07123456789")
    assert diary_entry.extract_mobile() == ["07123456789"]

"""
Given an extracted mobile number
Append number to a list of mobile numbers 
"""

def test_extract_mobile_numbers():
    mobile_numbers = []
    diary_entry = DiaryEntry("Tessa Cowan", "07123456789")
    diary_entry.extract_mobile(mobile_numbers)
    assert mobile_numbers == ["07123456789"]

# Run the test


5. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.