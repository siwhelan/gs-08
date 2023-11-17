from lib.track import *


# test creating a new track, should be able to get the artist and title back
def test_add_track_and_get_title_and_artist():
    track = Track("Title 1", "Artist 1")
    assert track.title == "Title 1"
    assert track.artist == "Artist 1"


# test format() returns a correctly formatted track
def test_format_artist_and_title():
    track = Track("Title 1", "Artist 1")
    assert track.format() == "Title 1 by Artist 1"
