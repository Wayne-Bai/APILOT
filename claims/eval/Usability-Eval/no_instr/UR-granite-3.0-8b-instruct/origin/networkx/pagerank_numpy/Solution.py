import networkx as nx

def page_rank(G, max_iter=100, tol=1.0e-6):
    """
    Compute the PageRank of the nodes in the graph G.

    Parameters:
    G (networkx.Graph): The graph to compute the PageRank for.
    max_iter (int): The maximum number of iterations to perform.
    tol (float): The tolerance for convergence.

    Returns:
    dict: A dictionary mapping node names to their PageRank scores.
    """
    # Initialize the PageRank scores to 1/N for each node.
    n = len(G)
    pr = {node: 1/n for node in G.nodes()}

    # Perform the PageRank iteration.
    for _ in range(max_iter):
        new_pr = pr.copy()
        for node in G.nodes():
            for neighbor in G.neighbors(node):
                new_pr[node] += pr[neighbor] / G.degree(neighbor)
        # Check for convergence.
        if max(new_pr.values()) - min(new_pr.values()) < tol:
            break
        pr = new_pr

    return pr
