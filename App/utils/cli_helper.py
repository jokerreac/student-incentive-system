def prompt_for_id(type, get_by_id_func):

    while True:
            selected_id = input(f"Select {type} ID: ")
            obj = get_by_id_func(selected_id)
            if obj is not None:
                return obj
            else:
                print(f"\nSelection does not exist. Please enter a valid {type} ID.")