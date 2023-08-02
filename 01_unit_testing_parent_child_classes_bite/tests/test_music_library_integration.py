from lib.music_library import MusicLibrary
from lib.track import Track

def test_adding_multiple_tracks():
    library = MusicLibrary()
    track_1 = Track("Starships", "Niki Minaj")
    track_2 = Track("Master of Puppets", "Metallica")
    track_3 = Track("Smile", "Lilly Allen")
    library.add(track_1)
    library.add(track_2)
    library.add(track_3)
    result = library.tracks
    assert result == [track_1, track_2, track_3]

def test_search_for_track():
    library = MusicLibrary()
    track_1 = Track("Starships", "Niki Minaj")
    track_2 = Track("Master of Puppets", "Metallica")
    track_3 = Track("Smile", "Lilly Allen")
    library.add(track_1)
    library.add(track_2)
    library.add(track_3)
    result = library.search("Master of Puppets")
    assert result == [track_2]

def test_Search_for_artist():
    library = MusicLibrary()
    track_1 = Track("Starships", "Niki Minaj")
    track_2 = Track("Master of Puppets", "Metallica")
    track_3 = Track("Smile", "Lilly Allen")
    track_4 = Track("Enter Sandman", "Metallica")
    library.add(track_1)
    library.add(track_2)
    library.add(track_3)
    library.add(track_4)
    result = library.search("Metallica")
    assert result == [track_2, track_4]