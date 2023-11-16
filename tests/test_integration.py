from lib.music_library import MusicLibrary
from lib.track import Track


# Test that when adding tracks to the library they
# can be recalled from the list
def test_adding_tracks_to_the_library():
    my_music = MusicLibrary()
    track_1 = Track("Track 1", "Artist 1")
    track_2 = Track("Track 2", "Artist 2")
    my_music.add(track_1)
    my_music.add(track_2)
    assert my_music.all() == [track_1, track_2]


# test ability to return a specific track when searching a library of 2 songs
def test_search_by_title():
    my_music = MusicLibrary()
    track_1 = Track("Track 1", "Artist 1")
    track_2 = Track("Track 2", "Artist 2")
    my_music.add(track_1)
    my_music.add(track_2)
    assert my_music.search_by_title("Track 2") == [track_2]


# test ability to return a specific track when searching a library of 2 songs
# only searching for part of the track
def test_search_by_part_of_title():
    my_music = MusicLibrary()
    track_1 = Track("Track 1", "Artist 2")
    track_2 = Track("Track 3", "Artist 4")
    my_music.add(track_1)
    my_music.add(track_2)
    assert my_music.search_by_title("3") == [track_2]
