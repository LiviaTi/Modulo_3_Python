def format_names(dictionary: dict) -> list:
    """
    Receives a dictionary of first and last names
    and returns a list of full names in uppercase letters.
    """
    full_names = []
    for first_name, last_name in dictionary.items():
        formatted_name = f"{first_name.capitalize()} {last_name.capitalize()}"
        full_names.append(formatted_name)
    return full_names