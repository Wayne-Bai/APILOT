import collections.abc

def is_iterator(obj):
    return isinstance(obj, collections.abc.Iterator)
