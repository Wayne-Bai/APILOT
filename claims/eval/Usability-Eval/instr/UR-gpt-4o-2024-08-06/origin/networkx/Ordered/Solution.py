import networkx as nx

class OrderedGraph(nx.Graph):
    def __init__(self, **attr):
        super().__init__(**attr)
        self.node_order = []
        self.edge_order = []

    def add_node(self, node_for_adding, **attr):
        if node_for_adding not in self.node_order:
            self.node_order.append(node_for_adding)
        super().add_node(node_for_adding, **attr)

    def add_edge(self, u_of_edge, v_of_edge, **attr):
        if (u_of_edge, v_of_edge) not in self.edge_order:
            self.edge_order.append((u_of_edge, v_of_edge))
        super().add_edge(u_of_edge, v_of_edge, **attr)

    def nodes(self):
        return iter(self.node_order)

    def edges(self, nbunch=None, data=False, default=None):
        return iter(self.edge_order)

class OrderedDiGraph(nx.DiGraph, OrderedGraph):
    def __init__(self, **attr):
        super().__init__(**attr)

class OrderedMultiGraph(nx.MultiGraph, OrderedGraph):
    def __init__(self, **attr):
        super().__init__(**attr)

class OrderedMultiDiGraph(nx.MultiDiGraph, OrderedGraph):
    def __init__(self, **attr):
        super().__init__(**attr)

# Example usage of the OrderedGraph
if __name__ == "__main__":
    G = OrderedGraph()
    G.add_node(1)
    G.add_node(2)
    G.add_edge(1, 2)
    G.add_node(3)
    G.add_edge(2, 3)
    
    print("Nodes in added order:")
    print(list(G.nodes()))
    
    print("Edges in added order:")
    print(list(G.edges()))
