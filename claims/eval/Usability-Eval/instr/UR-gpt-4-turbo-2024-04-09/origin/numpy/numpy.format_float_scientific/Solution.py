import numpy as np

def format_float_scientific(value):
    return f"{value:.6e}"

# Example usage
float_number = 0.000123
formatted_number = format_float_scientific(float_number)
print(formatted_number)
