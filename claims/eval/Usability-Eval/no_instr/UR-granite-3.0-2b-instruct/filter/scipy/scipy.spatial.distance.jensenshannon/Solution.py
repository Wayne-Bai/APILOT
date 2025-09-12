from scipy.stats import entropy

def jensen_shannon_distance(p, q):
    p = p / sum(p)
    q = q / sum(q)

    p_ent = entropy(p)
    q_ent = entropy(q)

    js_div = 0.5 * (entropy(p) + entropy(q))
    js_dist = 0.5 * (js_div + (p_ent + q_ent))

    return js_dist ** 0.5
