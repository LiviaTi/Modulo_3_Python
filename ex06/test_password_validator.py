import pytest
import password_validator

@pytest.mark.parametrize("password, result",[
    ("12345678", True),
    ("1234567", False),
    ("123456789", True),
    ("1234567891234567", True),
    ("12345678912345678", False)
])
def test_valid_size(password, result)-> bool:
    assert password_validator.valid_size(password) == result

@pytest.mark.parametrize("password, result",[
    ("Natali", True),
    ("nAtAli", True),
    ("natalI", True),
    ("natali", False)
])
def test_has_upper(password, result) -> bool:
    assert password_validator.has_upper(password) == result

@pytest.mark.parametrize("password, result",[
    ("NATaLI", True),
    ("NATaLi", True),
    ("nATALI", True),
    ("NATALI", False)
])
def test_has_lower(password, result) -> bool:
    assert password_validator.has_lower(password) == result

@pytest.mark.parametrize("password, result",[
    ("NATaLI1", True),
    ("NAT5aLi", True),
    ("nATA85LI", True),
    ("NATALI", False)
])
def test_has_digit(password, result) -> bool:
    assert password_validator.has_digit(password) == result

@pytest.mark.parametrize("password, result",[
    ("NATaLI1*", True),
    ("NAT!5aLi", True),
    ("nATA%85LI", True),
    ("NATAL}I", True),
    ("NATALI", False)
])
def test_has_especial_char(password, result) -> bool:
    assert password_validator.has_especial_char(password) == result

@pytest.mark.parametrize("password, result",[
    ("NATaLI1*", True),
    ("NAT!5aLi", True),
    (" nATA%85LI", False),
    ("NATAL}I ", False),
    ("NA TALI", False)
])
def test_is_clean_spaces(password, result) -> bool:
    assert password_validator.is_clean_spaces(password) == result
