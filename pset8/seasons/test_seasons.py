from seasons import valiDate, minutes
import pytest

def test_valiDate():
    with pytest.raises(SystemExit):
        valiDate("january 1, 1992")
        valiDate("2029-01-01")
        valiDate("2000-99-01")
        valiDate("2000-01-99")

