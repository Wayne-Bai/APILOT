import networkx as nx

def coverage_and_performance(G):
    # Calculate coverage
    coverage = nx.coverage(G)

    # Calculate performance
    performance = nx.performance(G)

    return coverage, performance
