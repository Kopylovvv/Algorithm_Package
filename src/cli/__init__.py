import typer

from src.cli.factorial_cmd import factorial_cmd
from src.cli.fibo_cmd import fibo_cmd
from src.cli.sort_cmd import sort_cmd
from src.cli.benchmark_cmd import benchmark_cmd
from src.cli.stack_cmd import stack_cli

app = typer.Typer(help="Алгоритмический мини пакет")

app.command("factorial")(factorial_cmd)
app.command("fibo")(fibo_cmd)
app.command("sort")(sort_cmd)
app.command("benchmark")(benchmark_cmd)
app.command("stack")(stack_cli)
