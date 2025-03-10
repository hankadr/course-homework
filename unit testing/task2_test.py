import pytest

from task2 import Number       

@pytest.mark.parametrize("value, expected_octal", [(42, '0o52'),(100, '0o144'),(255, '0o377')])
def test_to_octal(value, expected_octal):
    assert Number(value).to_octal() == expected_octal

@pytest.mark.parametrize("value, expected_hex", [(42, '0x2a'),(100, '0x64'),(255, '0xff')])
def test_to_hexadecimal(value, expected_hex):
    assert Number(value).to_hexadecimal() == expected_hex

@pytest.mark.parametrize("value, expected_binary", [(42, '0b101010'),(100, '0b1100100'),(255, '0b11111111')])
def test_to_binary(value, expected_binary):
    assert Number(value).to_binary() == expected_binary

@pytest.mark.parametrize("initial, new_value", [(10, 50),(0, 99),(-5, 25)])
def test_set_get_value(initial, new_value):
    num = Number(initial)
    num.set_value(new_value)
    assert num.get_value() == new_value

if __name__ == "__main__":
    pytest.main(["-v","--color=yes"])