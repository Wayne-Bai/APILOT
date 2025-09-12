import scipy
import scipy.stats

def lhs(n, samples):
    x = np.zeros((n, samples))
    for j in range(samples):
        order = np.random.permutation(n)
        u = np.random.uniform(size=n)
        x[:,j] = np.interp(u, np. cumulativesum(np.ones(n)/n), np.sort(np.random.uniform(size=n)))
    return x