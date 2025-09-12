import networkx as nx

def find_communities_greedy(G):
    # Create a copy of the graph to undirect any edges
    G = G.to_undirected()

    # Initialize a list to hold communities
    communities_generator = nx.community.greedy_modularity_communities(G)

    # Convert the generator to a list of sets
    communities = list(communities_generator)

    return communities
