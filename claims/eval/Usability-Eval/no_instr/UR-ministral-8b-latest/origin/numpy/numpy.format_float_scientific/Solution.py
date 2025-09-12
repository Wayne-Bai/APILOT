import numpy as np

def format_as_scientific_notation(number):
    formatted_number = np.format_float_scientific(number, trim='k')
    return formatted_number

# Example usage:
number_to_format = 1.23456789e20
formatted_number = format_as_scientific_notation(number_to_format)
print(formatted_number)
