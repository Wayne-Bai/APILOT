import numpy as np
from contextlib import contextmanager

@contextmanager
def preserve_random_state():
    seed = np.random.get_state()[0]
    try:
        yield
    finally:
        np.random.set_state(seed)
