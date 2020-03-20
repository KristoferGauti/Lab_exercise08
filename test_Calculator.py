from Calculator import Calculator

def test_add_empty_returns_zero() -> None:
    assert Calculator.Add("") == 0

def test_add_the_string_one_returns_int_one():
    assert Calculator.Add("1") == 1