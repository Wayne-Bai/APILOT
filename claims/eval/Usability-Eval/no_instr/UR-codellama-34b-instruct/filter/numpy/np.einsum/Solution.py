import numpy as np

def einstein_sum(operand1, operand2):
    """
    Evaluate the Einstein summation convention on the operands.

    Parameters:
        operand1 (numpy array): The first operand.
        operand2 (numpy array): The second operand.

    Returns:
        result (numpy array): The result of applying the Einstein summation convention to the operands.
    """
    # Check if the operands are numpy arrays
    if not isinstance(operand1, np.ndarray) or not isinstance(operand2, np.ndarray):
        raise ValueError("Both operands must be numpy arrays")

    # Get the shapes of the operands
    shape1 = operand1.shape
    shape2 = operand2.shape

    # Check if the shapes are compatible for the Einstein summation convention
    if len(shape1) != len(shape2):
        raise ValueError("The shapes of the operands must be equal")

    # Calculate the result using the Einstein summation convention
    result = np.einsum(operand1, operand2)

    return result
