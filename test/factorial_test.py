import math
from factorial import factorial

def test_factorial_range():
    for i in range(0, 100):
        assert factorial(i) == math.factorial(i)

def test_negative():
    import pytest

    with pytest.raises(ValueError):
        factorial(-1)