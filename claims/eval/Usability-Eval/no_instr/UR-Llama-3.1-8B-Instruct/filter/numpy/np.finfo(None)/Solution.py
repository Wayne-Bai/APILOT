import numpy as np

# Define a function to check machine limits for floating point types
def check_machine_limits():
    # Get the machine epsilon value (smallest value that can be added to 1 without causing an arithmetic error)
    machine_epsilon = np.finfo(np.float64).eps
    
    # Print machine epsilon value
    print("Machine epsilon value: ", machine_epsilon)
    
    # Get the maximum value that can be represented by a float64 (float)
    max_value = np.finfo(np.float64).max
    
    # Print maximum value
    print("Maximum value that can be represented by a float64: ", max_value)
    
    # Get the minimum value that can be represented by a float64 (float)
    min_value = np.finfo(np.float64).min
    
    # Print minimum value
    print("Minimum value that can be represented by a float64: ", min_value)
    
    # Get the maximum value that can be represented by a float32 (float)
    max_float32 = np.finfo(np.float32).max
    
    # Print maximum value
    print("Maximum value that can be represented by a float32: ", max_float32)
    
    # Get the minimum value that can be represented by a float32 (float)
    min_float32 = np.finfo(np.float32).min
    
    # Print minimum value
    print("Minimum value that can be represented by a float32: ", min_float32)

# Call the function
check_machine_limits()
