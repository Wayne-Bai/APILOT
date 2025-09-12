import scipy as sp
from scipy.stats import df, beta

# Function to compute the coefficient of variation
def compute_cv(data):
    mu = sp.mean(data)
    sigma = sp.stdev(data)
    cv = sigma / mu
    return cv

data = [1, 2, 3, 4, 5]
cv = compute_cv(data)
cv
