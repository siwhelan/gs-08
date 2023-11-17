from lib.diary import *
from lib.diary_entry import *


# test that when adding 2 entires, we can call them back
def test_diary_add_and_recall():
    diary = Diary()
    entry_1 = DiaryEntry("Entry 1 Title", "Contents 1")
    entry_2 = DiaryEntry("Entry 2 Title", "Contents 2")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == [entry_1, entry_2]


# add two entries, call count_words and have it return
# the total sum of words in the diary contents
def test_diary_count_words_returns_sum_of_all_words_in_entry_contents():
    diary = Diary()
    entry_1 = DiaryEntry("Entry 1 Title", "one two")
    entry_2 = DiaryEntry("Entry 2 Title", "three Four five")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_words() == 5


# Adding two entries with a total content length of 5 words, we can call
# reading_time with wpm of 2 and have it return '3' to represent the length of time
# it would take to read at that speed after rounding up
def test_reading_time_returns_3_minutes_to_read_5_words_at_2wpm():
    diary = Diary()
    entry_1 = DiaryEntry("Entry 1 Title", "one two")
    entry_2 = DiaryEntry("Entry 2 Title", "three Four five")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.reading_time(2) == 3


# test - adding two entries (1 short, 1 long) and a short wpm & reading time,
# reading_time must return thew shorter one as that's all we have time to read
def test_best_entry_to_read_returns_the_content_the_user_has_time_for():
    diary = Diary()
    entry_1 = DiaryEntry("Entry 1 Title", "one two")
    entry_2 = DiaryEntry("Entry 2 Title", "three Four five six seven eight nine ten")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2, 1) == entry_1


# test best entry for reading time returns the first entry the user has time to read
def test_find_best_entry_for_reading_time_returns_the_first_entry():
    diary = Diary()
    entry_1 = DiaryEntry("Entry 1 Title", "one two three")
    entry_2 = DiaryEntry(
        "Entry 2 Title", "one two three Four five six seven eight nine ten"
    )
    diary.add(entry_1)
    diary.add(entry_2)
    # 2wpm and 3 minutes of reading time would = 6 words max
    # function must return entry1 as the user does not have time to read 10 words
    assert diary.find_best_entry_for_reading_time(2, 3) == entry_1


# # test best entry for reading time returns the most suitable entry we have time to read
def test_find_best_entry_for_reading_time_returns_the_most_suitable_entry():
    diary = Diary()
    entry_1 = DiaryEntry("Entry 1 Title", "one two three")
    diary.add(entry_1)
    assert diary.find_best_entry_for_reading_time(2, 3) == entry_1


# test that when there are no possible entries due to time/length, the function returns None
def test_no_possible_entries_returns_none():
    diary = Diary()
    entry_1 = DiaryEntry("Entry 1 Title", "one two three four five six seven eight")
    diary.add(entry_1)
    assert diary.find_best_entry_for_reading_time(2, 3) == None


# test that the function returns the longer of two possible entries to read
def test_longer_of_two_readable_entries_is_returned():
    diary = Diary()
    entry_1 = DiaryEntry("Entry 1 Title", "one two")
    entry_2 = DiaryEntry("Entry 2 Title", "one two three Four five")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2, 3) == entry_2
