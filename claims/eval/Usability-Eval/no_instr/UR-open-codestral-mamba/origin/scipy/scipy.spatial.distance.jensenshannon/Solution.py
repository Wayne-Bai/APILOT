# First, we import the necessary modules from scipy
from scipy.spatial import distance
from scipy.special import kl_div, rel_entr
from scipy.stats import entropy

# Define the probability arrays
p = [0.1, 0.3, 0.6]
q = [0.2, 0.3, 0.5]

# We define a function to calculate the Jensen-Shannon distance
def jensen_shannon_distance(p, q):
    # calculate the individual Kullback–Leibler divergences
    kl_p_q = rel_entr(p, q)
    kl_q_p = rel_entr(q, p)

    # Sum the divergences
    sum_kl_p_q = sum(kl_p_q)
    sum_kl_q_p = sum(kl_q_p)

    # Return the Jensen-Shannon distance
    return (sum_kl_p_q + sum_kl_q_p) / 2

# Compute the Jensen-Shannon distance
jensen_shannon_distance(p, q)
