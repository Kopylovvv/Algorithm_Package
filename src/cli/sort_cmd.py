import typer

from src.algopack.utils.generators import (
    randint_array,
    nearly_sorted,
    many_duplicates,
    reverse_sorted,
)
from src.algopack.sorting_algorithms import (
    bubble_sort,
    quick_sort,
    counting_sort,
    radix_sort,
    bucket_sort,
    heap_sort,
)


def sort_cmd(
    algo: str = typer.Option(
        "quick",
        "--algo",
        "-a",
        help="Алгоритм: bubble|quick|counting|radix|bucket|heap",
    ),
    size: int = typer.Option(
        100,
        "--size",
        "-n",
        help="Размер массива",
    ),
    case: str = typer.Option(
        "random",
        "--case",
        "-c",
        help="Сценарий генерации: random|nearly_sorted|many_duplicates|reverse",
    ),
) -> None:
    """Отсортировать сгенерированный массив и вывести результат."""
    match case:
        case "random":
            data = randint_array(size, 0, size**2)
        case "nearly_sorted":
            data = nearly_sorted(size, max(1, size // 100))
        case "many_duplicates":
            data = many_duplicates(size)
        case "reverse":
            data = reverse_sorted(size)
        case _:
            raise typer.BadParameter("Такой сценарий генерации массива не поддерживается")

    match algo:
        case "bubble":
            result = bubble_sort(data)
        case "quick":
            result = quick_sort(data)
        case "counting":
            result = counting_sort(data)
        case "radix":
            result = radix_sort(data)
        case "heap":
            result = heap_sort(data)
        case "bucket":
            result = bucket_sort(data)
        case _:
            raise typer.BadParameter("Такой алгоритм сортировки не поддерживается")

    typer.echo(result)
