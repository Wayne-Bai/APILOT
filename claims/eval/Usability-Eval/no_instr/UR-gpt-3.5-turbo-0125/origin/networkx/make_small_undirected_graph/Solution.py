
import networkx as nx

def create_graph(graph_description):
    G = nx.Graph()
    
    nodes = set()
    edges = set()
    
    for line in graph_description.split('\n'):
        if line.startswith('v '):
            node = int(line.split()[1])
            nodes.add(node)
        elif line.startswith('e '):
            edge = tuple(map(int, line.split()[1:]))
            edges.add(edge)
     
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    
    return G

# Sample graph description format:
graph_description = '''
v 1
v 2
v 3
e 1 2
e 2 3
'''

graph = create_graph(graph_description)
print(graph.nodes)
print(graph.edges)
