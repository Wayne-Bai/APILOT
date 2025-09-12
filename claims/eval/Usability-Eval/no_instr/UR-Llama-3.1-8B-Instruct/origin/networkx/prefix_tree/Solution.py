import networkx as nx
import os

class PrefixTree:
    def __init__(self):
        self.G = nx.DiGraph()
        self.path_prefixes = set()

    def add_path(self, path):
        for i in range(len(path)):
            prefix = self._get_prefix(path, i)
            self.path_prefixes.add(prefix)
            self._add_node_to_graph(path[:i+1], prefix)

    def _get_prefix(self, path, end_index):
        return '/'.join(path[:end_index+1])

    def _add_node_to_graph(self, path, prefix):
        curr_node = 'root'
        for node in path:
            if curr_node not in self.G:
                self.G.add_node(curr_node)
            curr_node = node
            if curr_node not in self.G:
                self.G.add_node(curr_node)
            self.G.add_edge(curr_node, node)
        self.G.nodes[prefix]['visited'] = True

    def get_prefixes(self):
        # Return all prefix nodes
        return self.path_prefixes

    def draw_graph(self):
        pos = nx.spring_layout(self.G)
        labels = {node: node for node in self.G.nodes()}
        nx.draw_networkx_nodes(self.G, pos, node_size=700)
        nx.draw_networkx_labels(self.G, pos, labels=labels, font_size=10)
        nx.draw_networkx_edges(self.G, pos, arrowsize=20, arrows='->')
        # Display the edges
        plt.show()

# Usage:
tree = PrefixTree()
filePath = r'C:\test\test\test\test'
for r, d, f in os.walk(filePath):
    for file in f:
        path = os.path.join(r, file).split('\\')
        path = [p for p in path if p!= '']
        tree.add_path(path)
tree.draw_graph()
print(tree.get_prefixes())
