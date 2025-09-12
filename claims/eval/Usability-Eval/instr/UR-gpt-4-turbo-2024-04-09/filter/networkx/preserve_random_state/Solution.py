import numpy as np
import functools

def preserve_random_state(func):
    @functools.wraps(func)
    def wrapper_preserve_random_state(*args, **kwargs):
        state = np.random.get_state()
        try:
            result = func(*args, **kwargs)
        finally:
            np.random.set_state(state)
        return result
    return wrapper_preserve_random_state

# Example usage
@preserve_random_state
def random_operations():
    print("Generating random numbers:")
    print(np.random.rand(5))

# Testing the decorator
if __name__ == "__main__":
    print("Before any operations:")
    initial_state = np.random.get_state()
    np.random.seed(42)

    random_operations()

    print("\nAfter operations:")
    after_state = np.random.get_state()

    # Check if the state is preserved
    assert initial_state[1][0] == after_state[1][0], "Random state was not preserved!"
    print("Random state preserved successfully.")
