from lib.pjct_diary_class import *
from lib.pjct_diary_entry_class import *

class Diary():

    def test_add_diary_entries_to_diary():
        whole_diary = Diary()
        diary_entry1 = DiaryEntry("31 July", "Do some coding")
        diary_entry2 = DiaryEntry("1 August", "Go out with some old friends")
        whole_diary.add(diary_entry1)
        whole_diary.add(diary_entry2)
        whole_diary.entries == [diary_entry1, diary_entry2]

# """ 
# Given adding a new diary entry 
# We can add diary entry to diary 
# """

# def test_adding_an_entry(): 
#     whole_diary = Diary()
#     diary_entry1 = DiaryEntry("31 July", "Do some coding")
#     diary_entry2 = DiaryEntry("1 August", "Go out with some old friends")
#     whole_diary.add(diary_entry1)
#     whole_diary.add(diary_entry2)
#     assert whole_diary.entries == [diary_entry1, diary_entry2]


# """
# Given the word count of all the entries 
# Returns the total word count of the whole contents of the diary 
# """

# def test_count_total_words_for_whole_diary():
#     whole_diary = Diary()
#     diary_entry1 = DiaryEntry("31 July", "Do some coding")
#     diary_entry2 = DiaryEntry("1 August", "Go out with some old friends")
#     whole_diary.add(diary_entry1)
#     whole_diary.add(diary_entry2)
#     assert diary_entry1.count_words() == 3
#     assert diary_entry2.count_words() == 6
#     assert whole_diary.count_words() == 9


# """
# Given the reading time of all the entries 
# Returns the total reading time for the whole contents of the diary 
# """
# def test_add_total_reading_time_for_whole_diary():
#     whole_diary = Diary()
#     diary_entry1 = DiaryEntry("31 July", "Do some coding")
#     diary_entry2 = DiaryEntry("1 August", "Go out with some old friends")
#     whole_diary.add(diary_entry1)
#     whole_diary.add(diary_entry2)
#     assert diary_entry1.reading_time(200) == 0.015
#     assert diary_entry2.reading_time(200) == 0.03
#     assert whole_diary.reading_time(200) == 0.045

# """
# Given I add two entries, one long and one short
# And I call #find_best_entry_for_reading_time
# With a wpm and minutes that means I can only read the short one 
# Then #find_best_entry_for_reading_time returns the shorter one 
# """

# # def test_best_reading_chunk():
# #     whole_diary = Diary()
# #     diary_entry1 = DiaryEntry("31 July", "Do some coding")
# #     diary_entry2 = DiaryEntry("1 August", "Go out with some old friends Tuesday")
# #     whole_diary.add(diary_entry1)
# #     whole_diary.add(diary_entry2)
# #     assert whole_diary.find_best_entry_for_reading_time(2, 4) == diary_entry1

# """
# Given I add a diary entry
# And I call # find_best
# With a wpm and a minutes that means I can read that entry
# Then #find_best returns that entry 
# """

# def test_best_reading_chunk_that_fits():
#     whole_diary = Diary()
#     diary_entry1 = DiaryEntry("31 July", "Do some coding")
#     whole_diary.add(diary_entry1)
#     assert whole_diary.find_best_entry_for_reading_time(2, 3) == diary_entry1

# """
# Given I add a diary entry
# And I call # find_best
# With a wpm and a minutes that means I cannot read that entry
# Then #find_best returns None
# """

# def test_no_reading_chunk_suitable():
#     whole_diary = Diary()
#     diary_entry1 = DiaryEntry("1 August", "Go out with some old friends on Tuesday")
#     whole_diary.add(diary_entry1)
#     assert whole_diary.find_best_entry_for_reading_time(2, 3) == None

# """
# Given I add two entries
# And I call #find_best_entry_for_reading_time
# With a wpm and minutes that means I can read both 
# Then #find_best_entry_for_reading_time returns the longer one 
# """

# def test_best_reading_chunk_for_both():
#     whole_diary = Diary()
#     diary_entry1 = DiaryEntry("31 July", "Do some coding")
#     diary_entry2 = DiaryEntry("1 August", "Go out with some old friends Tuesday")
#     whole_diary.add(diary_entry1)
#     whole_diary.add(diary_entry2)
#     assert whole_diary.find_best_entry_for_reading_time(2, 4) == diary_entry2

# """
# Given a diary
# When we add diary entries 
# We see those entries reflected in the diary
# """
# diary = Diary()
# diary_entry_1 = DiaryEntry("Carte Blanche", "Veracocha")
# diary_entry2 = DiaryEntry("Synaesthesia", "The Thrillseekers")
# diary.add(diary_entry1)
# diary.add(diary_entry2)
# diary.diary_entry # => [diary_entry1, diary_entry2]