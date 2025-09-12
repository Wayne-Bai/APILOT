import numpy as np

try:
    # code that raises AxisError
    pass
except (ValueError, IndexError) as e:
    if isinstance(e, np.AxisError):
        print("Axis supplied was invalid.")