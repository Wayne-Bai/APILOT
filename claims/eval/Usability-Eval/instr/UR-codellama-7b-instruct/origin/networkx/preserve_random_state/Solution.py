
import contextlib
import numpy as np

def preserve_random_state(func):
    @contextlib.contextmanager
    def _preserve_random_state(*args, **kwargs):
        state = np.random.get_state()
        try:
            yield
        finally:
            np.random.set_state(state)
    return _preserve_random_state
