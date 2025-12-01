import random


def quick_sort(arr: list[int]) -> list[int]:
    """
    Quick sort
    """
    if len(arr) <= 1:
        return arr
    left = []
    middle = []
    right = []
    pivot = random.choice(arr)
    for elem in arr:
        if elem > pivot:
            right.append(elem)
        elif elem == pivot:
            middle.append(elem)
        else:
            left.append(elem)
    return quick_sort(left) + middle + quick_sort(right)
