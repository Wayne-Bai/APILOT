from werkzeug.exceptions import BadRequest

def create_dict_from_kwargs(**kwargs):
    """
    Bind the provided arguments into a dictionary.

    :param kwargs: The named arguments to convert into a dictionary.
    :return: A dictionary containing the provided keyword arguments.
    """
    return {key: value for key, value in kwargs.items()}

# Example usage
try:
    arguments = create_dict_from_kwargs(name='Werkzeug', version='2.0.0')
    print(arguments)
except Exception as e:
    print(f"An error occurred: {e}")
