from lib.secret_diary import SecretDiary
from lib.diary import Diary

def test_prevents_reading_when_locked():
    # Given a locked SecretDiary
    # It returns "Go away!"
    test_entry = Diary("This is a secret")
    test_diary = SecretDiary(test_entry)
    result = test_diary.read()
    assert result == "Go away!"

def test_gives_contents_when_unlocked():
    # Given an unlocked SecretDiary
    # It returns the contents of Diary.
    test_entry = Diary("This isn't a secret")
    test_diary = SecretDiary(test_entry)
    test_diary.unlock()
    result = test_diary.read()
    assert result == "This isn't a secret"

def test_blocks_contents_when_relocked():
    # Given an unlocked SecretDiary
    # It returns "Go away!" when locked again.
    test_entry = Diary("Just kidding, it's a secret")
    test_diary = SecretDiary(test_entry)
    test_diary.unlock()
    test_diary.lock()
    result = test_diary.read()
    assert result == "Go away!"
