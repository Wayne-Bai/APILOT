import numpy.random as rnd
from functools import wraps

def preserve_random_state(func):
    """Decorator to preserve the numpy.random state during a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        state = rnd.get_state()
        try:
            return func(*args, **kwargs)
        finally:
            rnd.set_state(state)
    return wrapper
