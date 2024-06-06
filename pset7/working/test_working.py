from working import convert
import pytest

def test_usr():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9-5")
    with pytest.raises(ValueError):
        convert("15:00 to 00:00")
    with pytest.raises(ValueError):
        convert("13:00 PM to 19:00 AM")

def test_single():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("1 PM to 3 AM") == "13:00 to 03:00"
    assert convert("12 AM to 5 PM") == "00:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"

def test_dbl():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:30 AM to 5:45 PM") == "09:30 to 17:45"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_12():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

