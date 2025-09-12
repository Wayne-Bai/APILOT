import networkx as nx

class PrefixTree:
    def __init__(self):
        self.tree = nx.DiGraph()

    def add_path(self, path):
        """Add a path to the prefix tree."""
        nodes = path.split('/')
        current_node = 'root'
        for node in nodes:
            if node:
                if not self.tree.has_edge(current_node, node):
                    self.tree.add_edge(current_node, node)
                current_node = node

    def get_prefix_tree(self):
        """Return the prefix tree as a networkx graph."""
        return self.tree

    def display_prefix_tree(self):
        """Display the prefix tree in a readable format."""
        for node in self.tree.nodes:
            print(node, end=' ')
            for neighbor in self.tree.neighbors(node):
                print('->', neighbor)
            print()

# Example usage:
prefix_tree = PrefixTree()
paths = ['/home/user/documents', '/home/user/images', '/home/user/videos']
for path in paths:
    prefix_tree.add_path(path)

print("Prefix Tree:")
prefix_tree.display_prefix_tree()
