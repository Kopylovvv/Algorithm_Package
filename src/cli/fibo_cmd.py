import typer

from src.algopack.math_funcs import fibo, fibo_recursive


def fibo_cmd(
    n: int,
    recursive: bool = typer.Option(
        False,
        "--recursive",
        "-r",
        help="Использовать рекурсивную версию",
    ),
) -> None:
    """Посчитать n-е число Фибоначчи."""
    result = fibo_recursive(n) if recursive else fibo(n)
    typer.echo(result)
