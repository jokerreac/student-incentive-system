# Student Incentive System

A Staff and Student system for recording hours of community service/volunteering.  

---

## Features

- Staff can log completed service hours for students  
- Students can request confirmation of completed service hours  
- Staff can approve or deny pending service requests  
- Students/Staff can view student leaderboard sorted by total approved hours  
- Students can view accolades earned for milestone hours (10/25/50+ hours)

---

## CLI Commands

### Table Inspection Commands

These commands help inspect the database tables:

| Command | Description |
|---------|-------------|
| `flask list-users` | Displays User table |
| `flask list-students` | Displays Student table |
| `flask list-staff` | Displays Staff table |
| `flask list-services` | Displays Service table |
| `flask list-accolades` | Displays Accolade table |
| `flask list-service-records` | Displays ServiceRecord table |
| `flask list-accolade-records` | Displays AccoladeRecord table |

### User Commands

Commands for interacting with the system as a student or staff:

| Command | Description |
|---------|-------------|
| `flask log-service-hours` | Staff only: Log completed service hours for a student |
| `flask request-service-log` | Student only: Request verification of completed service hours |
| `flask process-service-request` | Staff only: Approve or deny pending service requests |
| `flask view-leaderboard` | All users: View student leaderboard sorted by total approved hours |
| `flask view-accolades` | Student only: View accolades earned |

---

## Flask MVC Template
A template for flask applications structured in the Model View Controller pattern [Demo](https://dcit-flaskmvc.herokuapp.com/). [Postman Collection](https://documenter.getpostman.com/view/583570/2s83zcTnEJ)

## Dependencies
* Python3/pip3
* Packages listed in requirements.txt

## Installing Dependencies
```bash
$ pip install -r requirements.txt
```

## Initializing the Database
When connecting the project to a fresh empty database ensure the appropriate configuration is set then file then run the following command. This must also be executed once when running the app on heroku by opening the heroku console, executing bash and running the command in the dyno.

```bash
$ flask init
```