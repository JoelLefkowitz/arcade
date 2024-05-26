from src.app.scores import rank


def test_rank() -> None:
    assert rank(1) == "1st"
    assert rank(2) == "2nd"
    assert rank(3) == "3rd"
    assert rank(4) == "4th"

    assert rank(10) == "10th"
    assert rank(11) == "11th"
    assert rank(12) == "12th"
    assert rank(13) == "13th"
    assert rank(14) == "14th"

    assert rank(20) == "20th"
    assert rank(21) == "21st"
    assert rank(22) == "22nd"
    assert rank(23) == "23rd"
    assert rank(24) == "24th"
