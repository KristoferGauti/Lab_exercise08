from Calculator import Calculator

def test_add_empty_returns_zero() -> None:
    assert Calculator.Add("") == 0

def test_add_the_string_one_returns_int_one():
    assert Calculator.Add("1") == 1

def test_add_with_two_string_numbers_seperated_with_comma():
    assert Calculator.Add("1,2")

def test_add_with_two_string_numbers_seperated_with_comma_and_a_new_line():
    assert Calculator.Add("1\n2,3")