from src.algopack.sorting_algorithms.bubble import bubble_sort

E = 10 ** (-9)


def bucket_sort(arr: list[float], buckets: int | None = None) -> list[float]:
    """
    Bucket sort
    """

    if not arr:
        return []

    mn = min(arr)
    mx = max(arr)

    if mx == mn:
        return arr

    if buckets is None:
        buckets = int(len(arr) ** 0.5)

    if buckets == 1:
        bubble_sort(arr)
        return arr

    buckets_list = [[] for _ in range(buckets)]

    for elem in arr:
        buckets_list[int(buckets * (elem - mn) / (mx - mn + E))].append(elem)

    result = []
    for bucket in buckets_list:
        sorted_bucket = bucket_sort(bucket)
        result.extend(sorted_bucket)

    return result
