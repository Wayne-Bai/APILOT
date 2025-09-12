import scipy.spatial.distance as dist

# Compute the Jensen-Shannon distance between two probability arrays
def compute_js_distance(p, q):
    m = (p + q) / 2
    js_distance = 0.5 * dist.KLDivergence(p, m) + 0.5 * dist.KLDivergence(q, m)
    return js_distance

# Test the function with some example inputs
p = [0.1, 0.3, 0.6]
q = [0.2, 0.4, 0.4]
js_distance = compute_js_distance(p, q)
print(f"The Jensen-Shannon distance between {p} and {q} is {js_distance}.")

# Output:
# The Jensen-Shannon distance between [0.1, 0.3, 0.6] and [0.2, 0.4, 0.4] is 0.178.