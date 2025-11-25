from typing import Callable

import time


def timeit_once(func, *args, **kwargs) -> float:
    """
    Измерить время выполнения функции в секундах.
    """
    start = time.perf_counter()
    func(*args, **kwargs)
    end = time.perf_counter()
    return end - start


def benchmark_sorts(
        arrays: dict[str, list],
        algos: dict[str, Callable],
) -> dict[str, dict[str, float]]:
    """
    Тестирует сортировки на наборах массивов
    Возвращает словарь:
        {algo_name: {array_name: avg_time_seconds}}
    """

    results = {algo_name: {} for algo_name in algos}

    for algo_name, algo in algos.items():
        for arr_name, arr in arrays.items():

            results[algo_name][arr_name] = timeit_once(algo, list(arr))

    return results

