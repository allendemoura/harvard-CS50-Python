import fuel, pytest

def test_convert():
    with pytest.raises(ValueError):
        fuel.convert("poo")
        fuel.convert("mom")
        fuel.convert("1/mom")
        fuel.convert("a/b")
    with pytest.raises(ValueError):
        fuel.convert("2/1")
        fuel.convert("1.1/2")
        fuel.convert("-1/1")
    with pytest.raises(ZeroDivisionError):
        fuel.convert("1/0")
        fuel.convert("1/0.0")
    assert fuel.convert("1/2") == 50

def test_gauge():
    assert fuel.gauge(0) == 'E'
    assert fuel.gauge(1) == 'E'
    assert fuel.gauge(2) == '2%'
    assert fuel.gauge(100) == 'F'
    assert fuel.gauge(99) == 'F'
    assert fuel.gauge(98) == '98%'
