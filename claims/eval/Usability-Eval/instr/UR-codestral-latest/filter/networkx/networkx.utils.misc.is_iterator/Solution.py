from collections.abc import Iterator

def is_iterator(obj):
    return isinstance(obj, Iterator)
