import PYTEST

def test_cal_square_1():
    result = PYTEST.cal_square(5)
    assert result==25

def test_cal_square_2():
    result = PYTEST.cal_square(6)
    assert result==36

def test_cal_square_3():
    result = PYTEST.cal_square(7)
    assert result==49

