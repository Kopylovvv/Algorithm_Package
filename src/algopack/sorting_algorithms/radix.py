import random


def radix_sort(arr: list[int], base: int = 10) -> list[int]:
    """
    Radix sort
    Отрицательные не поддерживаются: при их наличии выбрасывается ValueError
    """
    if not arr:
        return []


    if any(x < 0 for x in arr):
        raise ValueError("radix_sort поддерживает только неотрицательные числа")

    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        arr = quick_by_digit(arr, exp, base)
        exp *= base

    return arr


def quick_by_digit(arr: list[int], exp: int, base: int) -> list[int]:
    """
    сортировка по разряду.
    """
    if len(arr) <= 1:
        return arr
    left = []
    middle = []
    right = []
    pivot = random.choice(arr) // exp % base
    for elem in arr:
        if elem // exp % base > pivot:
            right.append(elem)
        elif elem // exp % base == pivot:
            middle.append(elem)
        else:
            left.append(elem)
    return quick_by_digit(left, exp, base) + middle + quick_by_digit(right, exp, base)
