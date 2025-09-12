import numpy as np

def einstein_summation(op1, op2):
    """
    Evaluates the Einstein summation convention on the given operands.

    Args:
    op1 (np.ndarray): The first operand.
    op2 (np.ndarray): The second operand.

    Returns:
    np.ndarray: The result of the Einstein summation convention.
    """
    result = np.einsum('ij,ik->ijk', op1, op2)
    return result

# Example usage:
a = np.array([[1, 2], [3, 4]])
b = np.array([1, 2], [5, 6])

result = einstein_summation(a, b)
print(result)
