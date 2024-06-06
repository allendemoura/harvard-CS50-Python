from bank import value

def test_0():
    assert value("hello") == 0


def test_20():
    assert value("hey") == 20
    assert value("hell") == 20


def test_100():
    assert value("shine") == 100


def test_cap():
    assert value("Hello") == 0
    assert value("helLo") == 0
