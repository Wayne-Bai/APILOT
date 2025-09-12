
import networkx as nx

# Load the JIT JSON file into a NetworkX graph object
with open('graph.json') as f:
    G = nx.read_jit(f)

# Display the graph in the NetworkX GUI
nx.draw_networkx(G)
