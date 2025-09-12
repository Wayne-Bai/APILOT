import numpy as np

# Define a function to display machine limits for different floating point types
def display_machine_limits():
    # Define different floating point types
    float_types = [np.float16, np.float32, np.float64]

    # Iterate over each floating point type
    for float_type in float_types:
        # Display the floating point type
        print(f"Floating Point Type: {float_type.__name__}")

        # Display the smallest and largest possible values
        print(f"Smallest Possible Value: {np.finfo(float_type).min}")
        print(f"Largest Possible Value: {np.finfo(float_type).max}")

        # Display the smallest difference between two distinct floating point numbers
        print(f"Smallest Difference Between Two Distinct Floating Point Numbers: {np.finfo(float_type).eps}")

        # Display the machine epsilon value
        print(f"Machine Epsilon Value: {np.finfo(float_type).eps}")

        # Print a newline for better readability
        print("\n")

# Call the function to display machine limits
display_machine_limits()
