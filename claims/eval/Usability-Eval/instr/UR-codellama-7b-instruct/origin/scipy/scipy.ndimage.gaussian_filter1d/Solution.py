
def gaussian_filter1d(x, sig=None, n=None):
    """Apply a Gaussian filter to a one-dimensional array."""
    if sig is None:
        sig = n / (2 * np.sqrt(2 * np.log(2)))
    x_size = len(x)
    # normalize the filter to prevent overflows when computing weights
    norm = 1 / sps.ndimage.gaussian_filter(np.ones(x_size), sig)
    weights = np.exp(-0.5 * (np.arange(x_size) - x_size // 2 + 0.5) ** 2 / sig ** 2)
    return sps.ndimage.gaussian_filter(x, weights=norm * weights, mode='constant')
