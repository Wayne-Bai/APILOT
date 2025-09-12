def is_iterable_with_len(obj):
    return hasattr(obj, '__iter__') and hasattr(obj, '__len__')
