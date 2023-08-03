from lib.diary import Diary

def test_create_diary():
    # Given a string of contents
    # It creates an instance of diary entry with the given contents.
    test_entry = Diary("This is a test")
    result = test_entry.contents
    assert result == "This is a test"

def test_read_contents():
    # Given an instance of Diary
    # It returns the contents when the read method is called.
    test_entry = Diary("This is a test")
    result = test_entry.read()
    assert result == "This is a test"