def is_iterable_and_has_len(obj):
    try:
        iter(obj)
        return True if hasattr(obj, '__len__') else False
    except TypeError:
        return False
