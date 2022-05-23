from typing_extensions import assert_type
from third_challenge.lib import odd

def test_odd():
    number = 4
    assert odd(number) == False
    result = odd(number)
    assert isinstance(result, bool)
