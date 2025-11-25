import math
import pytest
from algopack.math_funcs import (
    factorial,
    factorial_recursive,
    fibo,
    fibo_recursive,
)


@pytest.mark.parametrize("n", [0, 1, 2, 5, 6, 10, 20, 50, 100])
def test_factorial(n: int) -> None:
    expected = math.factorial(n)
    assert factorial(n) == expected
    assert factorial_recursive(n) == expected


@pytest.mark.parametrize("n", [-1, -5, -100])
def test_factorial_raises(n: int) -> None:
    with pytest.raises(ValueError):
        factorial(n)
    with pytest.raises(ValueError):
        factorial_recursive(n)


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (10, 55),
        (20, 6765),
        (30, 832040),
    ],
)
def test_fibo(n: int, expected: int) -> None:
    assert fibo(n) == expected
    assert fibo_recursive(n) == expected


@pytest.mark.parametrize("n", [-1, -5, -100])
def test_fibo_raises(n: int) -> None:
    with pytest.raises(ValueError):
        fibo(n)
    with pytest.raises(ValueError):
        fibo_recursive(n)
