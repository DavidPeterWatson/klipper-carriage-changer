from carriage import Carriage
import pytest

def test_when_valid_then_does_not_throw():
    Carriage.validate_name('test')

def test_when_blank_then_does_throw():
    with pytest.raises(Exception) as exc_info:   
        Carriage.validate_name('')
    assert exc_info.value.args[0] == "Carriage name cannot be ''"
