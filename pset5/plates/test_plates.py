from plates import is_valid

def test_startletters():
    assert is_valid("1244") == False
    assert is_valid("C2456") == False



def test_maxmin():
    assert is_valid("CS50505") == False
    assert is_valid("C") == False

def test_num_middle():
    assert is_valid("AAA22A") == False
    assert is_valid("AAA022") == False


def test_punc():
    assert is_valid("AAA!22") == False
    assert is_valid("AAA 22") == False
    assert is_valid("CS50.") == False


def test_true():
    assert is_valid("CS50") == True
