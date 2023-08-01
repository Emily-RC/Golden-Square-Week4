
# File: lib/diary_entry.py

class DiaryEntry:
    def __init__(self, title, contents): 
        self.title = title
        self.contents = contents

    def count_words(self):
        word = self.contents.split()
        return len(word)

    def reading_time(self, wpm):
        words = self.contents.split()
        count_words = len(words)
        return count_words / 200
    
    def reading_chunk(self, wpm, minutes):
        words_per_minute = int(wpm)
        words_to_read = int(words_per_minute * minutes)
        words = self.contents.split()[:words_to_read]
        return " ".join(words)