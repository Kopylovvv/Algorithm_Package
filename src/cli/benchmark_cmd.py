import typer

from src.algopack.utils.generators import (
    randint_array,
    nearly_sorted,
    many_duplicates,
    reverse_sorted,
)
from src.algopack.utils.benchmark import benchmark_sorts
from src.algopack.sorting_algorithms import (
    bubble_sort,
    quick_sort,
    counting_sort,
    radix_sort,
    bucket_sort,
    heap_sort,
)


def benchmark_cmd(
    size: int = typer.Option(10**4, help="Размер массива"),
) -> None:
    """
    Бенчмарк всех сортировок на разных типах данных
    и вывод времён сортировки в консоль.
    """
    arrays = {
        "random": randint_array(size, 0, size),
        "nearly_sorted": nearly_sorted(size, swaps=max(1, size // 100)),
        "many_duplicates": many_duplicates(size, k_unique=5),
        "reverse_sorted": reverse_sorted(size),
    }

    algos = {
        "bubble": bubble_sort,
        "quick": quick_sort,
        "counting": counting_sort,
        "radix": radix_sort,
        "heap": heap_sort,
        "bucket": bucket_sort,
    }

    results = benchmark_sorts(arrays, algos)

    header = f"{'algo':<8}" + "".join(f"{name:>18}" for name in arrays.keys())
    typer.echo(header)
    typer.echo("–" * len(header))

    for algo_name, times in results.items():
        row = f"{algo_name:<8}" + "".join(f"{times[name]:>18.6f}" for name in arrays.keys())
        typer.echo(row)
