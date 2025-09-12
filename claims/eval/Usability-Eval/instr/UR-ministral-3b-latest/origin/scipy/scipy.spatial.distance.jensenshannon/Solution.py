import scipy.stats

# Function to compute Jensen-Shannon distance
def jensenshannon_distance(p1, p2):
    m = 0.5 * (scipy.stats.moment_skew(p1) + scipy.stats.moment_skew(p2))
    jensenshannon_distance = 0.5 * (scipy.stats.kstest(p1, 'norm')[1] + scipy.stats.kstest(p2, 'norm')[1])
    return m ** -1 / 2 * jensenshannon_distance

# Example usage
p1 = [0.2, 0.5, 0.3]
p2 = [0.4, 0.3, 0.3]
distance = jensenshannon_distance(p1, p2)
print(distance)
