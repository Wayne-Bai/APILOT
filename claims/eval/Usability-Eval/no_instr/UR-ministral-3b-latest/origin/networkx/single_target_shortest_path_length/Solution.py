import networkx as nx

# Function to compute the shortest path lengths to a target from all reachable nodes
def shortest_path_lengths_to_target(G, target):
    dist = {}
    for node in G.nodes():
        if node == target:
            dist[target] = 0
        else:
            dist[node] = float('inf')

    distance_map = collections.defaultdict(list)

    priority_queue = PriorityQueue()
    priority_queue.put((0, target))

    while not priority_queue.empty():
        current_distance, current_node = priority_queue.get()
        if current_node in dist and current_distance < dist[current_node]:
            # We found a shorter path to the current_node
            for neighbor in G.neighbors(current_node):
                new_path_length = current_distance + G[current_node][neighbor]['weight']
                if new_path_length < dist[neighbor] and neighbor != current_node:
                    dist[neighbor] = new_path_length
                    priority_queue.put((new_path_length, neighbor))
            distance_map[current_node] = current_distance

    return dist, distance_map

# Example usage:
G = nx.Graph()  # Define your graph here
target = 'target_node'
shortest_paths_dist, distance_map = shortest_path_lengths_to_target(G, target)

print("The shortest path lengths to the target from all reachable nodes:", shortest_paths_dist)
