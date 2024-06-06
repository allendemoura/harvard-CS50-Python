import twttr

def test_shorten():
    assert twttr.shorten("poopy") == "ppy"
    assert twttr.shorten("henry") == "hnry"
    assert twttr.shorten("judaism!") == "jdsm!"
    assert twttr.shorten("12 men") == "12 mn"
    assert twttr.shorten("AEIUO") == ""

