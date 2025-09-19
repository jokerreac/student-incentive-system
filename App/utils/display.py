from rich.table import Table
from rich.console import Console

console = Console()

def display_table(objects, columns, title=None):
    if not objects:
        console.print("No data to display.")
        return

    table = Table(title=title or "Table")
    for col in columns:
        table.add_column(col, justify="left")
    for obj in objects:
        row = [str(getattr(obj, col, "")) for col in columns]
        table.add_row(*row)
    console.print(table)