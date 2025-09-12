import contextlib
import numpy.random as rng

def preserve_rng(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with contextlib.ExitStack() as stack:
            stack.enter_context(rng.RandomState(42))
            try:
                func(*args, **kwargs)
            finally:
                stack.exit_context()
    return wrapper
