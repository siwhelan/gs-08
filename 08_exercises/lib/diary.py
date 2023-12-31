from math import ceil


class Diary:
    def __init__(self):
        self._diary = []

    def add(self, entry):
        #   Adds the entry to the entries list
        self._diary.append(entry)

    def all(self):
        # Returns a list of instances of DiaryEntry
        return self._diary

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        total_words = 0
        for entry in self._diary:
            total_words += entry.count_words()
        return total_words

    def reading_time(self, wpm):
        if self._diary == []:
            raise Exception("No entries!")
        word_count = self.count_words()
        return ceil(word_count / wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        if self._diary == []:
            raise Exception("No entries!")
        # find the max no of words that can be read in the time given
        max_words_read = wpm * minutes
        most_readable = None
        longest_so_far = 0
        # loop throgh the diary entries
        for entry in self._diary:
            # if the word count is less than or equal to
            # the max readable words in that time
            if entry.count_words() <= max_words_read:
                # if that word's count is longer than the existing longest entry
                if entry.count_words() > longest_so_far:
                    # reassign the current longest & most readable to that entry
                    most_readable = entry
                    longest_so_far = entry.count_words()
        return most_readable
