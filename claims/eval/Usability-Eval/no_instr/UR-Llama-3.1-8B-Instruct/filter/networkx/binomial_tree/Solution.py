import networkx as nx

class BinomialTree:
    def __init__(self, n):
        self.n = n
        self.G = nx.DiGraph()
        self.build_tree()

    def build_tree(self):
        for i in range(self.n):
            for j in range(i + 1):
                node = (i, j)
                if j > 0:
                    parent = (i-1, j-1)
                    self.G.add_edge(parent, node)
                    self.G.add_edge(parent, (i-1, j))
                if j < i:
                    children = [(i, j+1), (i, j)]
                    for child in children:
                        self.G.add_edge(node, child)

    def print_tree(self):
        for node in self.G.nodes:
            print(f"Node: {node}, Parents: {list(self.G.predecessors(node))}, Children: {list(self.G.successors(node))}")

# Usage:
binomial_tree = BinomialTree(3)
binomial_tree.print_tree()
