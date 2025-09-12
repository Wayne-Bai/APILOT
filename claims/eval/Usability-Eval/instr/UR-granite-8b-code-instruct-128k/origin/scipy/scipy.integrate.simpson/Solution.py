
from scipy.integrate import simps

def integrate_simpsons(y, x=None, dx=1):
    if x is None:
        x = np.arange(len(y)) * dx
    return simps(y, x)
