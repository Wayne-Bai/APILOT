
import numpy as np
from typing import Callable

def decorate_numpy_random(function: Callable):
    def wrapper(*args, **kwargs):
        # Save the current numpy random state before calling the function
        random_state = np.random.get_state()
        # Call the function and capture any output
        output = function(*args, **kwargs)
        # Restore the numpy random state to its previous value
        np.random.set_state(random_state)
        return output
    return wrapper
