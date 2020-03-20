from Calculator import Calculator

def test_add_empty_returns_zero():
    assert Calculator.Add("") == 0

def test_add_the_string_one_returns_int_one():
    assert Calculator.Add("1") == 1

def test_add_with_two_string_numbers_seperated_with_comma():
    assert Calculator.Add("1,2") == 3

def unknown_number_of_arguments_in_string():
    assert Calculator("1,2,3,4,5") == 15

def test_add_with_two_string_numbers_seperated_with_comma_and_a_new_line():
    assert Calculator.Add("1\n2,3") == 6

def test_add_with_zeros_between_numbers():
    assert Calculator.Add("1001,2")