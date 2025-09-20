import click, pytest, sys
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User, Student, Staff, Service, Accolade, ServiceRecord, StudentAccolade
from App.main import create_app
from App.controllers import ( initialize )
from App.utils.display import *
from App.utils.cli_helper import *


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()

    # Adds sample student data
    students = [
    Student(
        username="alice123",
        password="alicepass",
        first_name="Alice",
        last_name="Johnson"
    ),
    Student(
        username="bob_the_builder",
        password="bobpass",
        first_name="Bob",
        last_name="Smith"
    ),
    Student(
        username="charlie2025",
        password="charliepass",
        first_name="Charlie",
        last_name="Brown"
    ),
    Student(
        username="diana_p",
        password="dianapass",
        first_name="Diana",
        last_name="Prince"
    ),
    Student(
        username="edward99",
        password="edwardpass",
        first_name="Edward",
        last_name="Norton"
    )
    ]
    for user in students:
        db.session.add(user)

    # Adds sample staff data
    staff = [
        Staff(
        username="fiona_admin",
        password="fionapass",
        first_name="Fiona",
        last_name="Gallagher"
    ),
    Staff(
        username="george_dcit",
        password="georgepass",
        first_name="George",
        last_name="Michaels"
    )
    ]
    for user in staff:
        db.session.add(user)

    # Adds sample service data
    services = [
    Service(name="Beach Cleanup"),
    Service(name="Library Volunteering"),
    Service(name="Study Help Desk")
    ]
    for service in services:
        db.session.add(service)

    # Adds sample accolade data
    accolades = [
    Accolade(
        title="Helping Hand",
        description="Awarded for completing 10 hours of volunteer service",
        target_hours=10
    ),
    Accolade(
        title="Community Builder",
        description="Awarded for completing 25 hours of volunteer service",
        target_hours=25
    ),
    Accolade(
        title="Impact Maker",
        description="Awarded for completing 50 hours of volunteer service",
        target_hours=50
    )
    ]
    for accolade in accolades:
        db.session.add(accolade)

    db.session.commit()
    print('database intialized')

'''
User Commands
'''
# List commands to aid marker in testing

@app.cli.command("show-user-table", help="Displays User table")
def list_all_users():
     display_table(User.list(), ["id", "username", "password" ,"first_name", "last_name"], "User Table")

@app.cli.command("show-student-table", help="Displays Student table")
def list_students():
    display_table(Student.list(), ["id", "username", "password" ,"first_name", "last_name"], "Student Table")

@app.cli.command("show-staff-table", help="Displays Staff table")
def list_staff():
    display_table(Staff.list(), ["id", "username", "password" ,"first_name", "last_name"], "Staff Table")

@app.cli.command("show-service-table", help="Displays Service Table")
def list_services():
    display_table(Service.list(), ["id", "name"], "Service Table")

@app.cli.command("show-accolade-table", help="Displays Accolade table")
def list_accolades():
    display_table(Accolade.list(), ["id", "title", "description", "target_hours"], "Accolade Table")
    
@app.cli.command("show-servicerecord-table", help="Displays ServiceRecord table")
def list_service_records():
    display_table(ServiceRecord.list(),
          ["id", "student_id", "staff_id", "service_id", "num_hours", "request_date", "status", "processed_date"], "ServiceRecord Table")

@app.cli.command("show-studentaccolade-table", help="Displays StudentAccolade Table")
def list_student_accolade():
    display_table(StudentAccolade.list(), ["student_id", "accolade_id", "date_earned"], "StudentAccolade Table")




@app.cli.command("request-service-log")
def request_service_log():
    print(f"\n======== REQUEST SERVICE LOG MENU ========")

    if not display_users("Student", Student.list()):
        return
    
    student = prompt_for_id("Student", Student.get_by_id)

    if not display_users("Staff", Staff.list()):
        return
    
    staff_member = prompt_for_id("Staff", Staff.get_by_id)

    if not display_services(Service.list()):
        return
    
    service = prompt_for_id("Service", Service.get_by_id)

    print("\n")
    while True:
        num_hours = input(f"Enter hours of service for [{student.first_name} {student.last_name} - {service.name}]: ")
        if num_hours.isdigit() and int(num_hours) > 0:
            print("\n")
            break
        else:
            print("Invalid input. Please enter a positive integer.\n")

    ServiceRecord.create_service_record(student.id, staff_member.id, service.id, num_hours)