from lib.diary_entry import *


# test that a title and contents can be returned
def test_adding_entry_can_be_called_back():
    diary_entry = DiaryEntry("Title 1", "New entry contents")
    assert diary_entry.title == "Title 1"
    assert diary_entry.contents == "New entry contents"


# test that count_words sums the total contents of each entry
# i.e. a total of 5 words in contents returns 5
def test_diary_count_words_returns_sum_of_all_words():
    diary_entry = DiaryEntry("Entry 1 Title", "One two three Four five")
    assert diary_entry.count_words() == 5


# test reading_time with a wpm of 2 and five word content, it should return 3
def test_reading_time():
    diary_entry = DiaryEntry("Entry 1 Title", "One two three Four five")
    assert diary_entry.reading_time(2) == 3


# test A string representing a chunk of the contents that the user could
# read in the given number of minutes.
def test_readable_first_chunk():
    diary_entry = DiaryEntry("Entry 1 Title", "One two three Four five")
    assert diary_entry.reading_chunk(2, 1) == "One two"


# If called again, `reading_chunk` should return the next chunk,
# skipping what has already been read, until the contents is fully read.
def test_readable_second_chunk():
    diary_entry = DiaryEntry("Entry 1 Title", "One two three Four five")
    assert diary_entry.reading_chunk(2, 1) == "One two"
    assert diary_entry.reading_chunk(2, 1) == "three Four"
    assert diary_entry.reading_chunk(2, 1) == "five"


# The next call after that it should restart from the beginning.
def test_reading_chunk_resets_after_completion():
    diary_entry = DiaryEntry("Entry 1 Title", "One two three Four five")
    assert diary_entry.reading_chunk(2, 1) == "One two"
    assert diary_entry.reading_chunk(2, 1) == "three Four"
    assert diary_entry.reading_chunk(2, 1) == "five"
    assert diary_entry.reading_chunk(2, 1) == "One two"
