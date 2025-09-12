from scipy.spatial import distance

def jensenshannon_distance(P, Q):
    """
    Computes the Jensen-Shannon distance (metric) between two probability arrays.
    This is the square root of the Jensen-Shannon divergence.
    """
    P = np.array(P)
    Q = np.array(Q)
    P = P / P.sum()
    Q = Q / Q.sum()
    M = 0.5 * (P + Q)
    JSD = 0.5 * (distance.KL_divergence(P, M) + distance.KL_divergence(Q, M))
    return np.sqrt(JSD)
