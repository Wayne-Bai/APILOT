import numpy as np

class AxisError(Exception):
    """Axis supplied was invalid.

    This is raised whenever an axis parameter is specified that is larger than the number of array dimensions.
    For compatibility with code written against older numpy versions, which raised a mixture of ValueError
    and IndexError for this situation, this exception subclasses both to ensure that except ValueError and
    except IndexError statements continue to catch AxisError.
    """
    pass

# Example usage
arr = np.array([[1, 2], [3, 4]])
try:
    arr.shape[2]
except AxisError:
    print("AxisError: Axis supplied was invalid.")
