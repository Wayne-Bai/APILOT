import networkx as nx

def average_degree_connectivity(G):
    # California actually has roads named as "HT-920", but we will assume that there's a direct relation between the route numbers and the road degrees
    degrees = [G.degree(n) for n in G.nodes()]

    degrees_count = [0] * (max(degrees) + 1)
    for d in degrees:
        degrees_count[d] += 1

    avg_degree_conn = [sum([i * degrees_count[i] for i in range(len(degrees_count))]) / sum(degrees_count)]

    for k in range(1, len(degrees_count)):
        window_sum = sum(degrees_count[i] for i in range(k + 1))
        window_sum_count = sum(degrees_count[i] > 0 for i in range(k + 1))

        if window_sum_count > 0:
            avg_degree_conn.append(window_sum / window_sum_count)

    return avg_degree_conn

# We will now create a simple graph to demonstrate the function
G = nx.karate_club_graph()

print(average_degree_connectivity(G))
