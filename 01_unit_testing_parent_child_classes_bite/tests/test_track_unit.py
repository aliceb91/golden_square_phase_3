from lib.track import Track

def test_create_track():
    track = Track("She Blinded me with Science", "Thomas Dolby")
    result = {track.title: track.artist}
    assert result == {"She Blinded me with Science": "Thomas Dolby"}

def test_track_matches_keyword():
    track = Track("Master of Puppets", "Metallica")
    result = track.matches("Master of Puppets")
    assert result == True