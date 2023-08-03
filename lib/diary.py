# File: lib/diary.py

class Diary:
    def __init__(self):
        self.entries = []

    def add(self, entry):
        self.entries.append(entry)
    
    def all(self):
        return self.entries

    def count_words(self):
        total_words = 0
        for entry in self.entries:
            total_words += entry.count_words()
        return total_words

    def reading_time(self, wpm):
        total_reading_time = 0
        for entry in self.entries:
            total_reading_time += entry.reading_time(200)
        return total_reading_time

    def find_best_entry_for_reading_time(self, wpm, mins):
        words_the_user_could_read = wpm * mins 
        most_readable = None
        longest_found_so_far = 0
        for entry in self.entries: 
            if entry.count_words() <= words_the_user_could_read:
                if entry.count_words() > longest_found_so_far: 
                    most_readable = entry 
                    longest_found_so_far = entry.count_words()
        return most_readable 