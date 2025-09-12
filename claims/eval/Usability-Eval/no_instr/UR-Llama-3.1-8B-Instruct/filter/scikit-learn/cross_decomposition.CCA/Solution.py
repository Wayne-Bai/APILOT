# Import necessary modules from scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cross_decomposition import CCA
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV
from scipy.stats import pearsonr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Let's generate some example data
np.random.seed(0)
X = np.random.rand(100, 5)
y = np.random.rand(100, 2)

# Standardize the data using StandardScaler
scaler_X = StandardScaler()
scaler_y = StandardScaler()

X_scaled = scaler_X.fit_transform(X)
y_scaled = scaler_y.fit_transform(y)

# Apply PCA for dimensionality reduction
pca = PCA(n_components=4)
X_pca = pca.fit_transform(X_scaled)

# Perform Canonical Correlation Analysis (CCA)
cca = CCA(n_components=2)
X_cca, y_cca = cca.fit_transform(X_pca, y_scaled)

# Evaluate the model
mse_x = mean_squared_error(X, X_cca)
mse_y = mean_squared_error(y, y_cca)
print("MSE for X in CCA: ", mse_x)
print("MSE for Y in CCA: ", mse_y)

# With CCA 
X_factors = X_cca[:, 0]
y_factors = y_cca[:, 0]

pearson_coef, _ = pearsonr(X_factors, y_factors)
print("Pearson Correlation Coefficient: ", pearson_coef)

# Plot CCA components
plt.figure(figsize=(8, 8))
sns.scatterplot(data=pd.DataFrame(X_factors), x=0, y=1)
sns.scatterplot(data=pd.DataFrame(y_factors), x=0, y=1)
plt.xlabel("CCA Component 1 (X)")
plt.ylabel("CCA Component 1 (Y)")
plt.title("CCA - Scattered plot of canonical components")
plt.show()
