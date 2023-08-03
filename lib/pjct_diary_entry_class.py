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

    def reading_chunk(self, wpm, mins):
        words_per_minute = int(wpm)
        words_to_read = int(words_per_minute * mins) 
        words = self.contents.split()[:words_to_read]
        return " ".join(words)
    
    def is_digit(self, s):
        return s.isdigit() and len(s) == 11

    def extract_mobile(self):
        mobile_numbers = []
        i = 0
        while i < len(self.contents):
            if self.contents[i].isdigit():
                start = i
                while i < len(self.contents) and self.contents[i].isdigit():
                    i += 1
                if i - start == 11:
                    mobile_numbers.append(self.contents[start:i])
            else:
                i += 1
        return mobile_numbers



