
from networkx import generators as nx_generators

# Generate a random graph
G = nx_generators.random_graphs(n=50, m=200)

# Find communities using greedy modularity maximization
communities = nx_generators.greedy_modularity_maximization(G)
