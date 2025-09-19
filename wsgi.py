import click, pytest, sys
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User, Student, Staff, Service, Accolade, ServiceRecord, StudentAccolade
from App.main import create_app
from App.controllers import ( initialize )
from App.utils.display import ( display_table )


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
@app.cli.command("list-all-users", help="Displays User table")
def list_all_users():
    users = User.query.all()
    display_table(users, ["id", "username", "password" ,"first_name", "last_name"], "User Table")

@app.cli.command("list-students", help="Displays Student table")
def list_students():
    students = Student.query.all()
    display_table(students, ["id", "username", "password" ,"first_name", "last_name"], "Student Table")

@app.cli.command("list-staff", help="Displays Staff table")
def list_staff():
    staff = Staff.query.all()
    display_table(staff, ["id", "username", "password" ,"first_name", "last_name"], "Staff Table")

@app.cli.command("list-services", help="Displays Service Table")
def list_services():
    services = Service.query.all()
    display_table(services, ["id", "name"], "Service Table")

@app.cli.command("list-accolades", help="Displays Accolade table")
def list_accolades():
    accolades = Accolade.query.all()
    display_table(accolades, ["id", "title", "description", "target_hours"], "Accolade Table")
    
@app.cli.command("list-service-records", help="Displays ServiceRecord table")
def list_service_records():
    service_records = ServiceRecord.query.all()
    display_table(service_records,
                  ["id", "student_id", "staff_id", "service_id", "num_hours", "request_date", "processed_date"], "ServiceRecord Table")
    
@app.cli.command("list-student-accolades", help="Displays StudentAccolade Table")
def list_student_accolade():
    student_accolades = StudentAccolade.query.all()
    display_table(student_accolades, ["student_id", "accolade_id", "date_earned"], "StudentAccolade Table")

