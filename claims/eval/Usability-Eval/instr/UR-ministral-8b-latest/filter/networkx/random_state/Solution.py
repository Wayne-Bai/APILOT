import networkx as nx

# Decorator to generate a numpy.random.RandomState instance
def random_state_decorator(func):
    def wrapper(*args, **kwargs):
        random_state = numpy.random.RandomState()
        kwargs['random_state'] = random_state
        return func(*args, **kwargs)
    return wrapper

@random_state_decorator
def generate_barabasi_albert_graph(n, m):
    G = nx.barabasi_albert_graph(n, m, random_state=numpy.random.RandomState())
    return G

# Example usage
n = 10
m = 2
G = generate_barabasi_albert_graph(n, m)
print(G.nodes())
