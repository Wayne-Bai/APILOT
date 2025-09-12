import networkx as nx
import numpy as np
import functools

def generate_random_state(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        seed = kwargs.pop('seed', None)
        if seed is not None:
            random_state = np.random.RandomState(seed)
        else:
            random_state = np.random.RandomState()
        kwargs['random_state'] = random_state
        return func(*args, **kwargs)
    return wrapper

@generate_random_state
def example_function(random_state, *args, **kwargs):
    # Here you can use the random_state to generate random numbers
    print(random_state.rand(1))

# When calling the function, you can pass a seed
example_function(seed=1)
