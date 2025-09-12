from sklearn.covariance import GraphicalLassoCV
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate random data
# For the sake of example, let's assume a sample data generation procedure
num_samples = 100
num_features = 10
np.random.seed(0)
# Generate some data with a structure
X = np.random.randn(num_samples, num_features)

# Apply the GraphicalLassoCV to estimate the precision matrix
model = GraphicalLassoCV()
model.fit(X)

# Retrieve the estimated covariance and precision matrices
covariance_ = model.covariance_
precision_ = model.precision_

# Visualization of the covariance matrix
sns.heatmap(covariance_, cmap='coolwarm', center=0, square=True)
plt.title("Estimated Covariance Matrix")
plt.show()

# Visualization of the precision matrix
sns.heatmap(precision_, cmap='coolwarm', center=0, square=True)
plt.title("Estimated Precision Matrix (Inverse Covariance)")
plt.show()

# Output best alpha selected by cross-validation
print(f"Optimal L1 Penalty (alpha): {model.alpha_}")
