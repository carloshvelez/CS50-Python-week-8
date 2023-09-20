import seasons
from datetime import date
import pytest

def test_correctas():
    assert seasons.validar(str(date.today())) == date.today()

def test_incorrect_format():
    with pytest.raises(SystemExit):
        seasons.validar("1984-20-20")


def test_correct_format():
    assert seasons.cantar(date.today()) == "Zero minutes"


