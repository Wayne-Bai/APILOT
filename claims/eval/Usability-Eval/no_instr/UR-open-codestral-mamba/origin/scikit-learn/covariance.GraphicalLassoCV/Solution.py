from sklearn.covariance import LedoitWolf
from sklearn.datasets import make_spd_matrix

# Generate a random SPD matrix to fit the model
random_spd_matrix = make_spd_matrix(5, random_state=0)

# Create a LedoitWolf object with a 'fraction_of_zero_coeffs' coefficient set to 0.75
lw = LedoitWolf(fraction_of_zero_coeffs=0.75)

# Fit the model to the random SPD matrix
lw.fit(random_spd_matrix)

# Print the inverse covariance matrix learned by the model
print(lw.covariance_)
