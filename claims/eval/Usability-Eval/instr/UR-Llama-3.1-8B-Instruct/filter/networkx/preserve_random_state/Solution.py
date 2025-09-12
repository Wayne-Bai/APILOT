import networkx as nx
import numpy as np

class PreserveState:
    """
    A context manager that preserves the numpy random state during function execution.
    """

    def __init__(self, state):
        self.state = state
        self.psi = np.random.get_state()

    def __enter__(self):
        np.random.set_state(self.psi)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        np.random.set_state(self.state)


def preserve_random_state(func):
    """
    A decorator function that preserves the numpy random state during function execution.
    """
    def wrapper(*args, **kwargs):
        original_state = np.random.get_state()
        try:
            return func(*args, **kwargs)
        finally:
            np.random.set_state(original_state)
    return wrapper


# Example usage:

@preserve_random_state
def function_with_randomness():
    np.random.rand()
    # Do something that uses numpy randomness


def main():
    original_state = np.random.get_state()
    function_with_randomness()
    new_state = np.random.get_state()
    
    # Verify that the numpy random state is the same as before the function
    assert np.array_equal(original_state, new_state), "Random state has been modified"


if __name__ == "__main__":
    main()

# Example usage with PreserveState class
psi = np.random.get_state()
with PreserveState(psi):
    np.random.rand()
    # Do something that uses numpy randomness
