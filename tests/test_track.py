from lib.music_library import * 
from lib.track import *

"""
When we create a new track
We can get its title and artist back 
"""

def test_construct_track_and_get_title_and_artist():
    track = Track("My Title", "My Artist")
    assert track.title == "My Title"
    assert track.artist == "My Artist"
    # no brackets after title as we're accessing a property, instance variable

def test_formats_title_and_artists():
    track = Track("My Title", "My Artist")
    assert track.format() == "My Title by My Artist"