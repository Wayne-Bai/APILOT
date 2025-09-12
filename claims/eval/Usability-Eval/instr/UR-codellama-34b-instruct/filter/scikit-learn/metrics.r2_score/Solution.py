import numpy as np
from sklearn.metrics import r2_score

# Generate some sample data
n = 100
X = np.random.rand(n, 5)
y = np.random.rand(n)

# Fit a linear regression model to the data
from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
linreg.fit(X, y)

# Calculate the R-squared value
r2 = r2_score(y, linreg.predict(X))
print("R-squared:", r2)
