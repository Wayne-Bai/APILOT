import networkx as nx
from networkx.algorithms import community as nx_comm

# Create a graph
G = nx.karate_club_graph()

# Find communities using greedy modularity maximization
communities = list(nx_comm.greedy_modularity_communities(G))

# Print the communities
for i, comm in enumerate(communities):
    print(f"Community {i+1}: {sorted(comm)}")
