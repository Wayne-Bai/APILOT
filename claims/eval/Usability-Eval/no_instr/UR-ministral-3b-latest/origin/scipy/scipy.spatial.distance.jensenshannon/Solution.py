import scipy.stats as stats

def jensenshesn_distance(p, q):
    # Normalize the probabilities
    p = [x / sum(x) for x in [p, q]]
    q = [x / sum(x) for x in [p, q]]

    # Calculate the average of the two distributions
    average = [0.5 * (p[i] + q[i]) for i in range(len(p))]

    # Calculate the Jensen-Shannon Divergence
    JS_div = 0.5 * (stats.entropy(p, average) + stats.entropy(q, average))

    # Calculate the Jensen-Shannon Distance
    JS_dist = JS_div / 2.0
    return JS_dist

# Example usage
p = [0.3, 0.5, 0.2]
q = [0.2, 0.4, 0.4]
distance = jensenshesn_distance(p, q)
print(f'Jensen-Shannon Distance: {distance}')
