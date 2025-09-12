import networkx as nx

def build_prefix_trie(paths):
    trie = nx.DiGraph()

    for path in paths:
        node = trie
        for char in path:
            if char not in node:
                node[char] = nx.DiGraph()
            node = node[char]
        node['*'] = {}

    return trie

# Example usage
paths = [["a", "b", "c"], ["a", "z"], ["b", "d"], ["a", "b", "z"]]
prefix_trie = build_prefix_trie(paths)
print(nx.to_nestedests(prefix_trie))
