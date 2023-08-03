from lib.pjct_diary_entry_class import *

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

# """
# Given the wpm a read can read and the time that takes per entry
# Returns a string repping a chunk of the contents the reader can read in the given minutes 
# """

def test_reading_chunk():
    diary_entry = DiaryEntry("31 July", "Do some coding")
    text = "Do some coding"
    assert diary_entry.reading_chunk(200, 0.015) == text