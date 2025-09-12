from scipy import stats

def coefficient_of_variation(data):
    """
    Compute the coefficient of variation.

    Args:
        data (list or array): A list or array of numerical data.

    Returns:
        float: The coefficient of variation.
    """
    mean = sum(data) / len(data)
    variance = sum((x - mean)**2 for x in data) / len(data)
    return (variance / mean) ** 0.5
