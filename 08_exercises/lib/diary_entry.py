from math import ceil


class DiaryEntry:
    def __init__(self, title, contents):  # title, contents are strings
        #   Sets the title and contents properties
        self.title = title
        self.contents = contents
        self._saved_place = 0

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        return len(self.contents.split())

    def reading_time(self, wpm):
        # estimate of the reading time in minutes
        #  or the contents at the given wpm.
        return ceil(self.count_words() / wpm)

    def reading_chunk(self, wpm, minutes):
        # Calculate the total number of words that can be read in the given time.
        readable_words = wpm * minutes
        words = self.contents.split()
        # Calculate the endpoint of the chunk. It is the minimum of the sum of the current position
        # and the number of readable words, or the total length of the words list.
        # This prevents going beyond the list's length.
        end_point = min(self._saved_place + readable_words, len(words))
        # Join the words from the current position (_saved_place) to the endpoint
        # to form the readable chunk of text.
        readable_chunk = " ".join(words[self._saved_place : end_point])
        # Update the saved place to the new endpoint, marking the position up to which
        # the user has read.
        self._saved_place = end_point
        # Check if the reading has reached or exceeded the end of the contents.
        if self._saved_place >= len(words):
            # Reset the saved place to 0 to start from the beginning in the next call.
            self._saved_place = 0

        # Return the readable chunk of text.
        return readable_chunk
