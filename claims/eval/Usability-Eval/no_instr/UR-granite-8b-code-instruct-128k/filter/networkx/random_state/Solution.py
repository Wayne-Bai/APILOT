
import networkx as nx

def random_state_decorator(func):
    def wrapper(*args, **kwargs):
        random_state = np.random.RandomState()
        return func(random_state, *args, **kwargs)
    return wrapper

