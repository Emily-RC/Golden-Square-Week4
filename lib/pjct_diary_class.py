class Diary:
    
    def __init__(self):
        self.entries = []
        self.todos = []
        self.mobile_numbers = []

    def add(self, diary_entry):
        self.entries.append(diary_entry)

    def add_todo(self, todo):
        self.todos.append(todo)

    def view_all_entries(self):
        return self.entries
    
    def view_all_todos(self):
        return self.todos
    
    def incomplete_todos(self):
        incomplete_todos = []
        for todo in self.todos:
            if todo.status == "Incomplete":
                incomplete_todos.append(todo)
        return incomplete_todos
    
    def complete_todos(self):
        complete_todos = []
        for todo in self.todos:
            if todo.status == "Complete":
                complete_todos.append(todo)
        return complete_todos
        
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

    def best_chunk(self, wpm, mins):
        words_the_user_could_read = wpm * mins 
        most_readable = None 
        longest_found_so_far = 0
        for entry in self.entries: 
            if entry.count_words() <= words_the_user_could_read:
                if entry.count_words() > longest_found_so_far:
                    most_readable = entry 
                    longest_found_so_far = entry.count_words()
        return most_readable
