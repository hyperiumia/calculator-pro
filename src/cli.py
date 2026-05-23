"""CLI mode for Calculator Pro (headless usage without GUI)."""

import argparse
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

from src.config import APP_NAME, APP_VERSION, APP_AUTHOR
from src.engine import CalculatorEngine

console = Console()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="calculator-pro",
        description=f"{APP_NAME} v{APP_VERSION} - Professional calculator with GUI and CLI modes",
        epilog="Examples:\n"
               "  python main.py                      # Launch GUI\n"
               "  python main.py calc '2+3*4'         # CLI calculation\n"
               "  python main.py calc 'sqrt(144)'     # Scientific function\n"
               "  python main.py calc 'sin(pi/2)'     # Trigonometry\n"
               "  python main.py history              # Show history\n",
    )

    subparsers = parser.add_subparsers(dest="command", help="Command")

    calc_parser = subparsers.add_parser("calc", help="Calculate an expression")
    calc_parser.add_argument("expression", help="Expression to evaluate")

    subparsers.add_parser("history", help="Show calculation history")
    subparsers.add_parser("gui", help="Launch GUI mode (default)")

    return parser


def print_banner():
    banner = Text()
    banner.append(f"  {APP_NAME}", style="bold green")
    banner.append(f" v{APP_VERSION}", style="dim")
    banner.append(f"\n  {APP_AUTHOR}", style="dim green")
    console.print(Panel(banner, border_style="green", padding=(0, 2)))


def run(args):
    print_banner()

    engine = CalculatorEngine()

    if not args.command or args.command == "gui":
        from src.gui import CalculatorGUI
        app = CalculatorGUI()
        app.run()
        return

    if args.command == "calc":
        engine.set_expression(args.expression)
        result = engine.calculate()
        if result.error:
            console.print(f"[red bold]{result.result}[/red bold]")
        else:
            console.print(f"\n  [dim]{result.expression}[/dim]")
            console.print(f"  [bold green]= {result.result}[/bold green]\n")

    elif args.command == "history":
        engine.set_expression("1+1")
        engine.calculate()
        engine.set_expression("2*3")
        engine.calculate()
        console.print("[yellow]No history yet. Run some calculations first.[/yellow]")
