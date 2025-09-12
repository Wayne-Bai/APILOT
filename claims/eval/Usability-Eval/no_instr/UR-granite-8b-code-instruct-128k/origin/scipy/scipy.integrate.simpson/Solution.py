import scipy

def integrate_simpsons(y, x=None, dx=1):
    if x is None:
        x = np.arange(len(y)) * dx
    slope = np.diff(y) / np.diff(x)
    area = (np.sum(slope[::2]) + 4 * np.sum(slope[1::2]) + slope[-1]) * dx / 3
    return area