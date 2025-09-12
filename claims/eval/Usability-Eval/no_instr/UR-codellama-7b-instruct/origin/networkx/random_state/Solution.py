G.add_node(i)
for j in range(10):
    if j > i:
        G.add_edge(i, j)
