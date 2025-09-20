from rich.table import Table
from rich.console import Console


def display_table(objects, columns, title=None):
    console = Console()
    if not objects:
        console.print("\nNo data to display.")
        return

    table = Table(title=title or "Table")
    for col in columns:
        table.add_column(col, justify="left")
    for obj in objects:
        row = [str(getattr(obj, col, "")) for col in columns]
        table.add_row(*row)
    print("\n")
    console.print(table)
    

def display_users(type, users):
    print("\n")
    print(f"{f'{type} ID':<15} {'Name':<20}")
    print("-" * 40)

    if not users:
        print("No data to display.\n")
        return False
    
    for u in users:
        staff_name = f"{u.first_name} {u.last_name}"
        print(f"{u.id:<15} {staff_name:<20}")
    return True


def display_services(services):
    print("\n")
    print(f"{'Service ID':<15} {'Name':<20}")
    print("-" * 40)

    if not services:
        print("No data to display.\n")
        return False

    for s in services:
        print(f"{s.id:<15} {s.name:<20}")
    return True