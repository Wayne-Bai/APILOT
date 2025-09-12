import numpy as np

# Display machine limits for various floating point types
float_limits = {
    'float16': (np.finfo(np.float16).min, np.finfo(np.float16).max, np.finfo(np.float16).eps),
    'float32': (np.finfo(np.float32).min, np.finfo(np.float32).max, np.finfo(np.float32).eps),
    'float64': (np.finfo(np.float64).min, np.finfo(np.float64).max, np.finfo(np.float64).eps),
}

for dtype, limits in float_limits.items():
    print(f"{dtype}: Min={limits[0]}, Max={limits[1]}, Epsilon={limits[2]}")
