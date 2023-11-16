from lib.music_library import MusicLibrary
from lib.track import Track


# test that the list is initially empty
def test_initial_list_is_empty():
    my_music = MusicLibrary()
    assert my_music.all() == []


# test that an initial search returns an empty list
def test_initial_search_is_empty():
    my_music = MusicLibrary()
    assert my_music.search_by_title("Song 2") == []
