import numpy as np

# Function to display machine limits for floating point types
def display_machine_limits():
    float_info = {
        'float16': np.finfo(np.float16),
        'float32': np.finfo(np.float32),
        'float64': np.finfo(np.float64)
    }

    for dtype, info in float_info.items():
        print(f"Machine limits for {dtype}:")
        print(f"  - Epsilon: {info.eps}")
        print(f"  - Maximum: {info.max}")
        print(f"  - Minimum: {info.min}")
        print(f"  - Smallest positive norm: {info.tiny}")
        print()

display_machine_limits()
