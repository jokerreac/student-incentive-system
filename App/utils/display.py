from rich.table import Table
from rich.console import Console
from datetime import date

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
    print(f"{'Service ID':<15} {'Name':<20}")
    print("-" * 40)

    if not services:
        print("No data to display.\n")
        return False

    for s in services:
        print(f"{s.id:<15} {s.name:<20}")
    return True


def display_pending(service_records):
    print(f"{'Record ID':<12} {'Student':<25} {'Service':<30} {'Hours':<10} {'Request Date':<16} {'Status':<16}")
    print("-" * 110)

    if not service_records:
        print("No data to display. Exiting application...")
        return False
    
    for record in service_records:
        student_name = f"{record.student.first_name} {record.student.last_name} (ID: {record.student.id})"
        request_date = record.request_date.strftime('%Y-%m-%d')
        print(f"{record.id:<12} {student_name:<25} {record.service.name:<30} {record.num_hours:<10} {request_date:<16} {record.status:<16}")
    
    return True


def display_leaderboard(leaderboard):
    print(f"\n{'Rank':<10} {'Student':<30} {'Total Hours':<10}")
    print("-" * 55)

    if not leaderboard:
        print("No data to display. Exiting application...")
        return False
    
    rank = 0
    for student in leaderboard:
        rank += 1
        student_name =  f"{student['student'].first_name} {student['student'].last_name} (ID: {student['student'].id})"
        hours = student["hours"]

        print(f"{rank:<10} {student_name:<30} {hours:<10}")
    
    return True


def display_accolades(accolade_records):
    print(f"\n{'Date Earned':<16} {'Accolade':<25} {'Description':<48}")
    print("-" * 100)

    if not accolade_records:
        return False

    for record in accolade_records:
        accolade = record.accolade
        date_earned = record.date_earned.strftime('%Y-%m-%d')

        print(f"{date_earned:<16} {accolade.title:<25} {accolade.description:<48}")

    return True


    