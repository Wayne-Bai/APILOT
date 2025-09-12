
import networkx as nx

def assert_close(a, b, tol=1e-9):
    return abs(a - b) <= tol

def assert_all_close(a, b, tol=1e-9):
    return all(abs(x - y) <= tol for x, y in zip(a, b))
