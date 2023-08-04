from lib.mock_music_library import *
from lib.mock_track import * 

"""
When I add multiple tracks 
They are reflected in the tracks list
"""

def test_adds_and_lists_multiple_tracks():
    library = MusicLibrary()
    track_1 = Track("My Title 1", "My Artist 1")
    track_2 = Track("My Title 2", "My Artist 2")
    library.add(track_1)
    library.add(track_2)
    assert library.tracks == [track_1, track_2]

"""
When I add multiple tracks
And I search for a track title 
Then I get th matching track back 
"""

def test_searches_for_track_by_full_title():
    library = MusicLibrary()
    track_1 = Track("Dog", "Cat")
    track_2 = Track("Frog", "Toad")
    library.add(track_1)
    library.add(track_2)
    assert library.search("Dog") == [track_1]