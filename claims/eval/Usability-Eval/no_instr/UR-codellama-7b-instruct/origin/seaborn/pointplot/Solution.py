import pandas as pd
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from seaborn import lmplot, axes_grid

# Load the Boston housing dataset
boston = load_boston()
X = boston.data[:, :2]  # independent variables
y = boston.target  # dependent variable

# Train a linear regression model with polynomial features of degree 3
reg = LinearRegression(poly_features=True, degree=3)
reg.fit(X, y)

# Plot the point estimates and error bars for each feature using lmplot()
plt.figure(figsize=(12, 6))
grid = axes_grid.GridSpec(nrows=5, ncols=1, hspace=0.3)
ax1 = grid[0]
ax1.scatter(X[:, 0], y, c="r", label="Data")
ax1.plot(reg.intercept_, reg.coef_[0, :], "--", color="g", label="Linear Regression")
lmplot(X, y, ax=ax1)
ax1.set_title("Point Estimates and Error Bars")
