import click, pytest, sys
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User, Student, Staff, Service, Accolade, ServiceRecord, StudentAccolade
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize )


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

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands')

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
@click.argument("first_name")
@click.argument("last_name")
def create_user_command(username, password, first_name, last_name):
    create_user(username, password, first_name, last_name)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)