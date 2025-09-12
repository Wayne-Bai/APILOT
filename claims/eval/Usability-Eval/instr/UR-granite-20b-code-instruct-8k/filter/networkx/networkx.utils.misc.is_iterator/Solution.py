import networkx as nx

def is_iterator(obj):
    """Check whether an object is an iterator."""
    return isinstance(obj, (nx.classes.reportviews.NodeView,
                            nx.classes.reportviews.EdgeView,
                            nx.classes.reportviews.MultiEdgeView,
                            nx.classes.reportviews.OutEdgeView,
                            nx.classes.reportviews.InEdgeView,
                            nx.classes.reportviews. degreeView))
