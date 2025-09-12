import numpy as np

# Function to format a floating-point scalar as a decimal string in positional notation
def format_floating_point(number):
    # Convert the number to a string with 'n' decimal places
    formatted_number = f"{number:.10f}"  # Use 10 significant digits for positional notation
    return formatted_number

# Example usage
number = np.float64(3.141592653589793)
formatted_number = format_floating_point(number)
print(formatted_number)
