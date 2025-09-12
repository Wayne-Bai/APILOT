import networkx as nx
import numpy.random

def generate_random_state(func):
    def wrapper(*args, **kwargs):
        rng = numpy.random.RandomState()
        result = func(*args, **kwargs)
        return rng.randint(0, 1000, size=(result,))
    return wrapper

@generate_random_state
def my_function():
    # Your function code here
    pass
