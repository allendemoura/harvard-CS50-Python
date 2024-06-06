from numb3rs import validate

def test_true():
    assert validate(r"1.1.1.1")
    assert validate(r"1.1.1.0")
    assert validate(r"1.1.1.255")

def test_false():
    # assert not validate(r"-1.1.1.1")
    assert not validate(r"1.1.1.256")
    assert not validate(r"1.1.1.")
    assert not validate(r"123")
    assert not validate(r"64325.4.3.5")
    assert not validate(r"1.32")
    assert not validate(r"1.1.1")



