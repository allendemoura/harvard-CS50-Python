from um import count

def test_internal():
    assert count("uumumumumumumumuum") == 0

def test_punc():
    assert count("hello, um, world") == 1
    assert count("mom asy um popop, um, um? um!  um  um...  ") == 6

def test_none():
    assert count("greet") == 0
    assert count("thank you") == 0
    assert count("khartoum") == 0
    assert count("yummy") == 0

def test_case():
    assert count("um") == 1
    assert count("UM") == 1
