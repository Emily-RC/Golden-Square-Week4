1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.

Class One: 
User wants a diary where they can add in entries, view the entries, count the words, see the reading time and find best diary entry match for the reading time. 

Class Two: 
For each entry, format should be TITLE: CONTENT. User wants to be able to count words, find reading time and find a suitable reading chunk. 

2. Design the Class Interface
Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.

Diary: 

def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        pass

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        pass

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        pass

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.

Diary Entry: 
def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        pass

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        pass

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.


3. Create Examples as Tests
Make a list of examples of how the class will behave in different situations.

"""
When we add to diary entry we get the diary entries added to the diary in the right format 

all_diary = Diary()
diary_entry1 = DiaryEntry("31 July", "Do some coding")
diary_entry2 = DiaryEntry("1 August", "Go out with some old friends")
all_diary.add(diary_entry1)
all_diary.add(diary_entry2)
all_diary.entries => ["31 July", "Do some coding", "1 August", "Go out with some old friends"]

"""

When we view all diary entries they are returned in a specific format: 
all_diary = Diary()
diary_entry1 = DiaryEntry("31 July", "Do some coding")
diary_entry2 = DiaryEntry("1 August", "Go out with some old friends")
all_diary.count_words => diary_entry1 + diary_entry2

Function that counts words



Given a name and a task
#remind reminds the user to do the task
"""
reminder = Reminder("Kay")
reminder.remind_me_to("Walk the dog")
reminder.remind() # => "Walk the dog, Kay!"

"""
Given a name and no task
#remind raises an exception
"""
reminder = Reminder("Kay")
reminder.remind() # raises an error with the message "No task set."

"""
Given a name and an empty task
#remind still reminds the user to do the task, even though it looks odd
"""
reminder = Reminder("Kay")
reminder.remind_me_to("")
reminder.remind() # => ", Kay!"
​
Encode each example as a test. You can add to the above list as you go.
4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.