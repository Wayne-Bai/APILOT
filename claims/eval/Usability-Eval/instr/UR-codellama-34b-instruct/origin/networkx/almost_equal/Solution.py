
import networkx as nx

def assert_equal_within_tolerance(a, b, tolerance):
    """
    Asserts that two numbers (or two ordered sequences of numbers) are equal to each other within some tolerance.
    
    Parameters:
        a (float or array-like): The first number or sequence of numbers.
        b (float or array-like): The second number or sequence of numbers.
        tolerance (float): The maximum allowed difference between the two numbers or sequences.
    
    Returns:
        bool: True if the difference between `a` and `b` is less than or equal to `tolerance`, False otherwise.
    """
    return nx.is_close(a, b, atol=tolerance)
