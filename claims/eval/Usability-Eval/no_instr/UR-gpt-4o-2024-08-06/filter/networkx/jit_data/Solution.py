import networkx as nx

def create_jit_json(G):
    # Function to convert NetworkX graph to JIT JSON format

    tree = []

    def add_children(node, parent):
        children = []
        for neighbor in G.neighbors(node):
            if neighbor != parent:
                child = {
                    "id": neighbor,
                    "name": str(neighbor),
                    "data": {},
                    "children": []
                }
                # Recursively add the children
                child["children"] = add_children(neighbor, node)
                children.append(child)
        return children

    # Assuming the graph G is a tree, we start from an arbitrary root node
    root_node = list(G.nodes)[0] if G.nodes else None

    if root_node is not None:
        # Create the root node in JIT JSON format
        root = {
            "id": root_node,
            "name": str(root_node),
            "data": {},
            "children": add_children(root_node, None)
        }
        tree.append(root)

    return tree

# Example usage with a simple tree graph
if __name__ == "__main__":
    G = nx.DiGraph()
    G.add_edges_from([(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)])

    jit_json = create_jit_json(G)
    print(jit_json)
