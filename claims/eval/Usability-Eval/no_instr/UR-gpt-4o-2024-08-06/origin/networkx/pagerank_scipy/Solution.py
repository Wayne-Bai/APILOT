import networkx as nx

def calculate_pagerank(graph):
    # Compute PageRank values for the nodes in the graph
    pagerank = nx.pagerank(graph)
    return pagerank

# Example of how to create a graph and use the function
if __name__ == "__main__":
    # Create a directed graph
    G = nx.DiGraph()
    
    # Add edges to the graph (representing links between nodes)
    edges = [("A", "B"), ("A", "C"), ("B", "C"), 
             ("C", "A"), ("D", "C"), ("E", "D"),
             ("F", "E"), ("B", "F")]
    G.add_edges_from(edges)
    
    # Calculate PageRank
    pagerank_values = calculate_pagerank(G)
    
    # Output PageRank values
    for node, rank in pagerank_values.items():
        print(f"Node {node}: PageRank {rank:.4f}")
