import numpy as np

# Floating point types
float_types = [np.float16, np.float32, np.float64]

# Machine limits
for t in float_types:
    print(f"Type: {t}")
    print(f"Minimum value: {np.finfo(t).min}")
    print(f"Maximum value: {np.finfo(t).max}")
    print(f"Epsilon (machine precision): {np.finfo(t).eps}")
    print(f"Resolution (smallest positive difference between two consecutive values): {np.finfo(t).resolution}")
    print()
