import networkx as nx
from math import log

def pagerank(G, alpha=0.85, max_iter=100, tol=1.0e-6):
    n = G.number_of_nodes()
    pr = dict.fromkeys(G.nodes(), 1.0 / n)

    for n_iter in range(max_iter):
        pr_new = dict(pr)
        d = dict.fromkeys(G.nodes(), 0.0)

        for v in G.nodes():
            for w in G.predecessors(v):
                d[w] += pr[w]

            if d.get(v, 0):
                pr_new[v] = pr[v] + alpha * d[v]
            else:
                pr_new[v] = pr[v]

            pr_new[v] += (1 - alpha) / n

        err = 0.0
        for v in pr:
            err += abs(pr[v] - pr_new[v])

        pr = pr_new
        if err < tol:
            break

    return pr
