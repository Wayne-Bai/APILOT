import networkx as nx

def is_iterator(obj):
    return isinstance(obj, (nx.classes.reportviews.ReportView, nx.classes.function.Function))
