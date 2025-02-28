# Test cases generated using LANGUAGE_MODEL=qwen2.5-coder:1.5b

import pytest

# Test cases for add function
@pytest.mark.parametrize("x, y, expected", [
    (1, 2, 3),
    (-1, -2, -3),
    (0, 0, 0),
    (5, 3, 8)
])
def test_add(x, y, expected):
    result = add(x, y)
    assert result == expected, f"Expected {expected}, got {result}"

# Test cases for mult function
@pytest.mark.parametrize("x, y, expected", [
    (1, 2, 2),
    (-1, -2, 2),
    (0, 0, 0),
    (5, 3, 15)
])
def test_mult(x, y, expected):
    result = mult(x, y)
    assert result == expected, f"Expected {expected}, got {result}"
