import networkx as nx
import numpy as np

def generate_random_state(func):
    def wrapper(*args, **kwargs):
        random_state = np.random.RandomState()
        return func(random_state, *args, **kwargs)
    return wrapper

# Example of how to use the decorator
@generate_random_state
def example_function(random_state, other_arguments):
    # Your code here
    # You can use random_state to generate random numbers
    pass
