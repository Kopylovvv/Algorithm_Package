import random

import pytest

from algopack.sorting_algorithms import (
    bubble_sort,
    quick_sort,
    counting_sort,
    radix_sort,
    bucket_sort,
    heap_sort,
)

INT_ARRAYS = [
    [],
    [1],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [2, 3, 2, 1, 3, 1],
    [0, 0, 0, 0],
    list(range(10)),
    list(range(10, 0, -1)),
    list(range(40, 95, 4))
]


def random_int_array(size: int, lo: int = -10000, hi: int = 10000) -> list[int]:
    return [random.randint(lo, hi) for _ in range(size)]


@pytest.mark.parametrize("arr", INT_ARRAYS + [random_int_array(1000)])
def test_int_sort(arr):
    sorted_arr = sorted(arr)
    unsorted_arr = arr.copy()
    assert bubble_sort(unsorted_arr) == sorted_arr
    unsorted_arr = arr.copy()
    assert quick_sort(unsorted_arr) == sorted_arr
    unsorted_arr = arr.copy()
    assert heap_sort(unsorted_arr) == sorted_arr
    unsorted_arr = arr.copy()
    assert counting_sort(unsorted_arr) == sorted_arr
    unsorted_arr = arr.copy()
    assert bucket_sort(unsorted_arr) == sorted_arr


@pytest.mark.parametrize(
    "arr",
    [
        [],
        [0, 1, 2, 3],
        [3, 1, 0, 2],
        [5, 5, 0, 1, 2],
        [10, 0, 3, 7, 7, 1],
        [0, 0, 0],
        [123, 4, 56, 789, 10],
    ],
)
def test_radix_sort_non_negative(arr):
    assert radix_sort(arr) == sorted(arr)


@pytest.mark.parametrize("arr", [[-1, 0, 1], [-10], [-5, 5]])
def test_radix_sort_raises_on_negative(arr):
    with pytest.raises(ValueError):
        radix_sort(arr)
