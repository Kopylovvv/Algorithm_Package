import typer

from src.algopack.math_funcs import factorial, factorial_recursive


def factorial_cmd(
        n: int,
        recursive: bool = typer.Option(
            False,
            "--recursive",
            "-r",
            help="Использовать рекурсивную версию",
        ),
) -> None:
    """Посчитать факториал числа n."""
    result = factorial_recursive(n) if recursive else factorial(n)
    typer.echo(result)
