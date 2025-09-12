import networkx as nx

class PrefixTree:
    def __init__(self):
        self.tree = nx.DiGraph()

    def add_path(self, path):
        """Add a path to the prefix tree."""
        path = path.split('/')  # Split the path into components
        path = [component for component in path if component!= '']  # Remove empty components

        node = 'ROOT'  # Start at the root node
        for component in path:
            # Check if the node already exists in the tree
            if not self.tree.has_edge(node, component):
                self.tree.add_edge(node, component)  # Add the edge to the tree
            node = component  # Move to the next node

    def visualize_tree(self):
        """Visualize the prefix tree."""
        nx.draw(self.tree, with_labels=True)

    def get_common_prefix(self, path1, path2):
        """Get the common prefix between two paths."""
        path1 = path1.split('/')  # Split the paths into components
        path1 = [component for component in path1 if component!= '']
        path2 = path2.split('/')
        path2 = [component for component in path2 if component!= '']

        common_prefix = []
        for component1, component2 in zip(path1, path2):
            if component1 == component2:  # Check if the components match
                common_prefix.append(component1)
            else:
                break

        return '/' + '/'.join(common_prefix)


# Example usage
if __name__ == "__main__":
    prefix_tree = PrefixTree()
    paths = ['/home/user/documents', '/home/user/pictures', '/home/user/videos']

    for path in paths:
        prefix_tree.add_path(path)

    prefix_tree.visualize_tree()  # Visualize the prefix tree
    common_prefix = prefix_tree.get_common_prefix(paths[0], paths[1])
    print(common_prefix)
