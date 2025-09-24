def prompt_for_id(type, get_by_id_func):

    while True:
            selected_id = input(f"Select {type} ID: ")
            obj = get_by_id_func(selected_id)
            if obj is not None:
                return obj
            else:
                print(f"Selection does not exist. Please enter a valid {type} ID.\n")


def prompt_for_hours(student, service):
     
     while True:
        num_hours = input(f"Enter hours of service for [{student.first_name} {student.last_name} - {service.name}]: ")
        if num_hours.isdigit() and int(num_hours) > 0:
            return num_hours
        else:
            print("Invalid input. Please enter a positive integer.\n")
