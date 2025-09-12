import networkx as nx

def check_iterable_with_len(obj):
    try:
        # Try to access the len of the object
        _ = len(obj)
        # Check if the obj has __getitem__ and __len__ methods to determine if it is iterable
        if hasattr(obj, '__getitem__') and hasattr(obj, '__len__'):
            return True
        else:
            return False
    except TypeError:
        return False

# Test the function
print(check_iterable_with_len('Hello, World!'))   # True because str is iterable
print(check_iterable_with_len([1,2,3,4,5]))  # True because list is iterable
print(check_iterable_with_len({1: 'one', 2: 'two', 3: 'three'}))  # True because dict is iterable
print(check_iterable_with_len(123))   # False because int is not iterable
