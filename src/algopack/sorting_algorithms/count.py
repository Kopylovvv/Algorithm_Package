def counting_sort(arr: list[int]) -> list[int]:
    """
    Counting sort
    """
    if not arr:
        return []

    mn = min(arr)
    mx = max(arr)
    k = mx - mn + 1
    counts = [0] * k

    for x in arr:
        counts[x - mn] += 1

    result = [(num+mn) for num, count in enumerate(counts) for _ in range(count)]
    return result
