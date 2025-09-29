import click, pytest, sys
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User, Student, Staff, Service, Accolade, ServiceRecord, AccoladeRecord
from App.main import create_app
from App.controllers import ( initialize )
# Cli helpers
from App.utils.display import *
from App.utils.prompt import *


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
        Service(name="Study Help Desk"),
        Service(name="Lab Tech Support"),
        Service(name="Library Assistance"),
        Service(name="Orientation Helper"),
        Service(name="Student Club Support")
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
        ),
        Accolade(
            title="Service Champion",
            description="Awarded for completing 75 hours of volunteer service",
            target_hours=75
        ),
        Accolade(
            title="Volunteer Legend",
            description="Awarded for completing 100 hours of volunteer service",
            target_hours=100
        )
    ]
    for accolade in accolades:
        db.session.add(accolade)

    db.session.commit()
    print('database intialized')

'''
List commands to aid marker in checking tables
'''

@app.cli.command("list-users", help="Displays User table")
def list_all_users():
    if not display_table(User.list(), ["id", "username", "password" ,"first_name", "last_name"], "User Table"):
        print("\nThere are currently no records in [User]\n")

@app.cli.command("list-students", help="Displays Student table")
def list_students():
    if not display_table(Student.list(), ["id", "username", "password" ,"first_name", "last_name"], "Student Table"):
        print("\nThere are currently no records in [Student]\n")

@app.cli.command("list-staff", help="Displays Staff table")
def list_staff():
    if not display_table(Staff.list(), ["id", "username", "password" ,"first_name", "last_name"], "Staff Table"):
        print("\nThere are currently no records in [Staff]\n")

@app.cli.command("list-services", help="Displays Service Table")
def list_services():
    if not display_table(Service.list(), ["id", "name"], "Service Table"):
        print("\nThere are currently no records in [Service]\n")

@app.cli.command("list-accolades", help="Displays Accolade table")
def list_accolades():
    if not display_table(Accolade.list(), ["id", "title", "description", "target_hours"], "Accolade Table"):
        print("\nThere are currently no records in [Accolade]\n")
    
@app.cli.command("list-service-records", help="Displays ServiceRecord table")
def list_service_records():
    if not display_table(ServiceRecord.list(),
          ["id", "student_id", "staff_id", "service_id", "num_hours", "request_date", "status", "processed_date"], "ServiceRecord Table"):
        print("\nThere are currently no records in [ServiceRecord]\n")

@app.cli.command("list-accolade-records", help="Displays AccoladeRecord Table")
def list_accolade_record():
    if not display_table(AccoladeRecord.list(), ["student_id", "accolade_id", "date_earned"], "AccoladeRecord Table"):
        print("\nThere are currently no records in [AccoladeRecord]\n")

'''
User commands
'''

@app.cli.command("log-service-hours", help="Log completed service hours for a student (staff only).")
def log_student_hours():
    print(f"\n======== LOG SERVICE HOURS MENU ========")
    print("\n")

    if not display_users("Staff", Staff.list()):
        return
    print("\n")
    
    staff_member = prompt_for_id("Staff", Staff.get_by_id)
    print("\n")

    if not display_users("Student", Student.list()):
        return
    print("\n")

    student = prompt_for_id("Student", Student.get_by_id)
    print("\n")

    if not display_services(Service.list()):
        return
    print("\n")
    
    service = prompt_for_id("Service", Service.get_by_id)
    print("\n")

    num_hours = prompt_for_hours(student, service)

    service_record = staff_member.log_service_hours(student.id, service.id, num_hours)
    print(f"\nService Record Created! (ID: {service_record.id})\n")

    accolade_records = student.award_accolades()
    display_accolade_unlocked(accolade_records)


@app.cli.command("request-service-log", help="Request confirmation of completed service hours (student only).")
def request_service_log():
    print(f"\n======== REQUEST SERVICE LOG MENU ========")
    print("\n")

    if not display_users("Student", Student.list()):
        return
    print("\n")

    student = prompt_for_id("Student", Student.get_by_id)
    print("\n")

    if not display_users("Staff", Staff.list()):
        return
    print("\n")
    
    staff_member = prompt_for_id("Staff", Staff.get_by_id)
    print("\n")

    if not display_services(Service.list()):
        return
    print("\n")
    
    service = prompt_for_id("Service", Service.get_by_id)
    print("\n")

    num_hours = prompt_for_hours(student, service)
    
    service_record = student.request_service_log(staff_member.id, service.id, num_hours)
    print(f"\nService Request Created! (ID: {service_record.id})\n")


@app.cli.command("process-service-request", help="Approve or deny pending service requests (staff only).")
def process_service_request():
    print(f"\n======== PROCESS SERVICE REQUEST MENU ========")
    print("\n")

    if not display_users("Staff", Staff.list()):
        return
    
    print("\n")
    staff_member = prompt_for_id("Staff", Staff.get_by_id)
    staff_name = staff_member.get_name()

    print(f"\n\nService Requests awaiting action for [{staff_name}]:\n")
    if not display_pending(ServiceRecord.list_pending_by_staff_id(staff_member.id)):
        print(f"{staff_name} has no requests at the moment.")
        return

    print("\n")
    while True:
        service_record = prompt_for_id("Record", ServiceRecord.get_by_id)
        if service_record.staff.id == staff_member.id and service_record.status == "Pending":
            break
        else:
            print(f"\nSelection does not exist. Please enter a valid Record ID.")

    while True:
        action = input(f"\nApprove request ({service_record.id}) [{service_record.student.get_name()} - {service_record.service.name} - {service_record.num_hours}.0 Hours] ? (a = approve, d = deny, c = cancel): ")
        
        if action == "a":
            staff_member.process_service_request(service_record, "Approved")
            break
        elif action == "d":
            staff_member.process_service_request(service_record, "Denied")
            break
        elif action == "c":
            print("\nOperation cancelled. Exiting application...")
            return
        else:
            print("Invalid input. Please choose from the provided options.")

    print(f"\nSuccessfully Processed Request (ID: {service_record.id}) - {service_record.status}!\n")

    accolade_records = service_record.student.award_accolades()
    display_accolade_unlocked(accolade_records)


@app.cli.command("view-leaderboard", help="View student leaderboard sorted by total approved hours (all users).")
def view_leaderboard():
    print("\nDisplaying leaderboard:\n")
    display_leaderboard(User.get_leaderboard())


@app.cli.command("view-accolades", help="View accolades earned by a student (student only).")
def view_accolades():
    print(f"\n======== VIEW ACCOLADES MENU ========")
    print("\n")

    if not display_users("Student", Student.list()):
        return
    print("\n")

    student = prompt_for_id("Student", Student.get_by_id)
    student_name = student.get_name()

    print(f"\n\nDisplaying Accolades for [{student_name}]:")

    if not display_accolades(student.get_accolades()):
        print(f"{student_name} has not earned any Accolades yet.")
        return