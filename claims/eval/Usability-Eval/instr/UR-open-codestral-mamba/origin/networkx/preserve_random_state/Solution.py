import networkx
import numpy as np
import functools

class RandomStateManager:
    """Preserves the numpy.random state during a function."""

    def __init__(self):
        self._state = np.random.get_state()

    def __enter__(self):
        np.random.set_state(self._state)

    def __exit__(self, exit_type, exit_value, exit_traceback):
        np.random.set_state(self._state)

def preserve_random_state(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with RandomStateManager():
            return func(*args, **kwargs)
    return wrapper

