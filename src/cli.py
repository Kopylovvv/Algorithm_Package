import typer

from src.algopack.math_funcs import (
    factorial,
    factorial_recursive,
    fibo,
    fibo_recursive,
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

