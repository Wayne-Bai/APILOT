import scipy.signal

def impulse_response(coefficients, num_samples=50):
    """Compute the impulse response of a linear system.

    Parameters:
        coefficients (list or tuple): Filter coefficients from worst delay to
                                      oldest.  output[n] == coefficients[0]*in[n]
                                      + coefficients[1]*in[n-1] + ....
        num_samples (int, optional): The length of the impulse response. Defaults
                                     to 50.

    Returns:
        numpy.ndarray: Impulse response with length num_samples.
    """
    return scipy.signal.lfilter(coefficients, [1], [1]+[0]*(num_samples-1))[1:]

# Example usage
coefficients = [0.5, 0.2]
print(impulse_response(coefficients, num_samples=10))
