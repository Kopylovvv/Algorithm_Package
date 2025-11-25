import typer

from src.algopack.stack_list import Stack


def stack_cli() -> None:
    """
    Интерактивная работа со стеком: push <x>, pop, peek, min, size, empty, exit.
    """
    s = Stack()
    typer.echo("Интерактивный стек. Команды: push <x>, pop, peek, min, size, empty, exit.")

    while True:
        try:
            line = input("> ").strip()
        except EOFError:
            break

        if not line:
            continue

        parts = line.split()
        cmd = parts[0].lower()

        match cmd:
            case "exit":
                break

            case "push":
                if len(parts) != 2:
                    typer.echo("Использование: push <int>")
                    continue
                try:
                    value = int(parts[1])
                except ValueError:
                    typer.echo("Ошибка: значение должно быть целым числом.")
                    continue
                s.push(value)
                typer.echo(f"OK, push {value}")

            case "pop":
                try:
                    value = s.pop()
                    typer.echo(f"pop -> {value}")
                except IndexError as e:
                    typer.echo(f"Ошибка: {e}")

            case "peek":
                try:
                    value = s.peek()
                    typer.echo(f"top -> {value}")
                except IndexError as e:
                    typer.echo(f"Ошибка: {e}")

            case "min":
                try:
                    value = s.min()
                    typer.echo(f"min -> {value}")
                except IndexError as e:
                    typer.echo(f"Ошибка: {e}")

            case "size":
                typer.echo(f"size -> {len(s)}")

            case "empty":
                typer.echo(f"empty -> {s.is_empty()}")

            case _:
                typer.echo("Неизвестная команда. Доступно: push, pop, peek, min, size, empty, exit.")
