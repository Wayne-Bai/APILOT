import networkx as nx

def hits_authority_matrix(G):
    # Initialize authority and hub scores
    hub_scores = dict(G.degree())
    authority_scores = dict.fromkeys(hub_scores, 1)

    # Max iterations
    max_iterations = 100

    for iteration in range(max_iterations):
        new_hub_scores = dict()
        new_authority_scores = dict(authority_scores)

        for node in G.nodes:
            new_hub_scores[node] = sum(authority_scores[neighbor] for neighbor in G.neighbors(node))

        for node in G.nodes:
            new_authority_scores[node] = sum(hub_scores[neighbor] for neighbor in G.neighbors(node))

        if new_hub_scores == hub_scores and new_authority_scores == authority_scores:
            break

        hub_scores = new_hub_scores
        authority_scores = new_authority_scores

    return hub_scores, authority_scores

# Example usage
G = nx.path_graph(5)
G.add_edge(2, 3)
hits_authority_matrix(G)
