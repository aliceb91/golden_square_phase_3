from lib.secret_diary import SecretDiary
from unittest.mock import Mock

def test_create_secret_diary():
    # Given an instance of Diary
    # It creates an instance of SecretDiary containing Diary.
    test_entry = Mock()
    test_diary = SecretDiary(test_entry)
    result = test_diary.diary
    assert result == test_entry

def test_default_value_locked():
    # Given an instance of SecretDiary
    # It defaults to a locked state on creation.
    test_entry = Mock()
    test_diary = SecretDiary(test_entry)
    result = test_diary.locked
    assert result == True

def test_read_returns_go_away_when_locked():
    # Given a locked instance of SecretDiary
    # It returns the string "Go away!"
    test_entry = Mock()
    test_diary = SecretDiary(test_entry)
    result = test_diary.read()
    assert result == "Go away!"

def test_unlock_opens_diary():
    # Given a locked instance of SecretDiary
    # It unlocks the diary when the unlock method is called.
    test_entry = Mock()
    test_diary = SecretDiary(test_entry)
    test_diary.unlock()
    result = test_diary.locked
    assert result == False

def test_return_contents_when_unlocked():
    # Given an unlocked instance of SecretDiary
    # It returns the contents of Diary when read is called.
    test_entry = Mock()
    test_entry.read.return_value = "This isn't a secret"
    test_diary = SecretDiary(test_entry)
    test_diary.unlock()
    result = test_diary.read()
    assert result == "This isn't a secret"

def test_blocks_contents_when_relocked():
    # Given an unlocked instance of SecretDiary
    # It locks the diary and returns "Go away!" when read is called.
    test_entry = Mock()
    test_diary = SecretDiary(test_entry)
    test_diary.unlock()
    test_diary.lock()
    result = test_diary.read()
    assert result == "Go away!"
