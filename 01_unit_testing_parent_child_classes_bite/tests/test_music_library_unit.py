from lib.music_library import MusicLibrary

class TestAddTrack():
    pass

class TestSearchTrackTrue():
    def matches(self, keyword):
        return True
    
class TestSearchTrackFalse():
    def matches(self, keyword):
        return False

def test_add_track():
    track = TestAddTrack()
    library = MusicLibrary()
    library.add(track)
    result = library.tracks
    assert result == [track]

def test_search_for_track():
    track_1 = TestSearchTrackFalse()
    track_2 = TestSearchTrackTrue()
    track_3 = TestSearchTrackFalse()
    library = MusicLibrary()
    library.add(track_1)
    library.add(track_2)
    library.add(track_3)
    result = library.search("Hello")
    assert result == [track_2]
    