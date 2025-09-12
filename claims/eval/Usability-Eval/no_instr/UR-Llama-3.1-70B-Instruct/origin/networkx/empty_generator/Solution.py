import networkx as nx
import matplotlib.pyplot as plt

class GraphGenerator:
    def __init__(self):
        self.G = nx.Graph()

    def add_node(self, node):
        self.G.add_node(node)

    def add_edge(self, node1, node2):
        self.G.add_edge(node1, node2)

    def print_graph(self):
        pos = nx.spring_layout(self.G)
        nx.draw(self.G, pos, with_labels=True, node_color='lightblue', node_size=5000)
        plt.show()

    def get_nodes(self):
        return list(self.G.nodes)

    def get_edges(self):
        return list(self.G.edges)

# Usage:
generator = GraphGenerator()
generator.add_node(1)
generator.add_node(2)
generator.add_node(3)
generator.add_edge(1, 2)
generator.add_edge(2, 3)
generator.add_edge(3, 1)
print("Nodes:", generator.get_nodes())
print("Edges:", generator.get_edges())
generator.print_graph()
