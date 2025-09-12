
import json
from networkx import read_jit

# Reading a graph from a JIT JSON file
with open('graph.json', 'r') as f:
    data = json.load(f)

G = read_jit(data)
