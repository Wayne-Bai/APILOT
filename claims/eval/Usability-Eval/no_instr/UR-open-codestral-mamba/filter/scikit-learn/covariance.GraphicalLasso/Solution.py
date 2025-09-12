from sklearn.covariance import LedoitWolf

# Create a LedoitWolf shrunk covariance estimator with an l1-penalized estimator
lw = LedoitWolf(store_precision=False, assume_centered=False)

# Fit the model with your data
# lw.fit(your_data)

# Now you can access the estimated covariance using lw.covariance_
