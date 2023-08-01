from lib.diary import *
from lib.diary_entry import *

"""
Initially
There is no diary entry  
"""

def test_initially_has_no_diary_entry():
    whole_diary = Diary()
    assert whole_diary.all() == []

