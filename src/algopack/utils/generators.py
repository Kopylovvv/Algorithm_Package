import random


def randint_array(
    n: int,
    lo: int,
    hi: int,
    distinct: bool = False,
    seed: int | None = None,
) -> list[int]:
    """
    Случайный массив целых чисел из [lo, hi]
    n: кол-во элементов в массиве
    lo: нижняя граница генерации
    hi: верхняя граница генерации
    distinct=True - элементы не повторяются
    distinct=False(по умолчанию) - элементы могут повторяться
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if lo > hi:
        raise ValueError("lo must be <= hi")

    rng = random.Random(seed)

    if distinct:
        if hi - lo + 1 < n:
            raise ValueError("range too small for distinct values")
        return rng.sample(range(lo, hi + 1), n)

    return [rng.randint(lo, hi) for _ in range(n)]


def nearly_sorted(
    n: int,
    swaps: int,
    seed: int | None = None,
) -> list[int]:
    """
    отсортированный массив с swaps изменениями
    n: кол-во элементов в массиве
    swaps: кол-во изменений в массиве
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if swaps < 0:
        raise ValueError("swaps must be non-negative")

    rng = random.Random(seed)
    arr = list(range(n))

    for _ in range(swaps):
        i = rng.randrange(n)
        j = rng.randrange(n)
        arr[i], arr[j] = arr[j], arr[i]

    return arr


def many_duplicates(
    n: int,
    k_unique: int = 5,
    seed: int | None = None,
) -> list[int]:
    """
    Массив состоящий из конечного числа уникальных элементов
    n: длина массива
    k_unique: кол-во уникальных элементов
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if k_unique <= 0:
        raise ValueError("k_unique must be positive")

    rng = random.Random(seed)
    values = [rng.randint(0, 100) for _ in range(k_unique)]
    return [rng.choice(values) for _ in range(n)]


def reverse_sorted(n: int) -> list[int]:
    """
    Массив отсортированный по убыванию
    n: кол-во элементов массива
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    return list(range(n, 0, -1))


def randfloat_array(
    n: int,
    lo: float = 0.0,
    hi: float = 1.0,
    seed: int | None = None,
) -> list[float]:
    """
    Массив вещественных чисел
    n: кол-во элементов массива
    lo: нижняя граница генерации
    hi: верхняя граница генерации
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if lo >= hi:
        raise ValueError("lo must be < hi")

    rng = random.Random(seed)
    return [rng.uniform(lo, hi) for _ in range(n)]

