import networkx as nx

def preserve_random_state(func):
    def wrapper(*args, **kwargs):
        state = np.random.get_state()
        result = func(*args, **kwargs)
        np.random.set_state(state)
        return result
    return wrapper
