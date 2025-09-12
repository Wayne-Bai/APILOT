import numpy as np

def format_float_as_decimal_string(value):
    # Ensure the value is a float
    if not isinstance(value, float):
        raise ValueError("Input must be a float.")
    
    # Format the float as a decimal string
    decimal_string = f"{value:.10f}"  # You can adjust the precision as needed
    return decimal_string

# Example usage
float_value = 123.456789
formatted_string = format_float_as_decimal_string(float_value)
print(formatted_string)
