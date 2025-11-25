import typer

from src.algopack.stack_list import Stack

from src.algopack.math_funcs import (
    factorial,
    factorial_recursive,
    fibo,
    fibo_recursive,
)

from src.algopack.sorting_algorithms import (
    bubble_sort,
    quick_sort,
    counting_sort,
    radix_sort,
    bucket_sort,
    heap_sort
)

app = typer.Typer(help="Алгоритмический мини-пакет: факториал, Фибоначчи, сортировки.")

@app.command("factorial")
def factorial_cmd(
    n: int,
    recursive: bool = typer.Option(False, "--recursive", "-r", help="Использовать рекурсивную версию"),
):
    """Посчитать факториал числа n."""
    result = factorial_recursive(n) if recursive else factorial(n)
    typer.echo(result)

@app.command("fibo")
def fibo_cmd(
    n: int,
    recursive: bool = typer.Option(False, "--recursive", "-r", help="Использовать рекурсивную версию"),
):
    """Посчитать n-е число Фибоначчи."""
    result = fibo_recursive(n) if recursive else fibo(n)
    typer.echo(result)

@app.command("sort")
def sort_cmd(
    algo: str = typer.Option("bubble", help="bubble|quick|counting|radix|bucket|heap"),
    size: int = typer.Option(10, help="Размер целочисленного массива"),
):
    """Отсортировать сгенерированный массив выбранным алгоритмом и вывести результат."""
    data = list(range(size, 0, -1))  # пока простой пример
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
            raise typer.BadParameter(f"Такой алгоритм сортировки не поддерживается")
    typer.echo(result)

@app.command("stack-demo")
def stack_demo() -> None:
    """
    Простейшая демонстрация работы стека.
    """
    s = Stack()
    for x in [1, 2, 3]:
        s.push(x)
    typer.echo(f"Stack size: {len(s)}")
    typer.echo(f"Top element: {s.peek()}")
    while not s.is_empty():
        typer.echo(f"Popped: {s.pop()}")
