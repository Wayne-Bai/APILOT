# Importing the required libraries
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import plot_partial_dependence
import matplotlib.pyplot as plt

# Load the diabetes dataset
diabetes = load_diabetes()
X, y = diabetes.data, diabetes.target

# Fitting a random forest regressor
rf = RandomForestRegressor(n_estimators=1000, random_state=0)
rf.fit(X, y)

# Plotting the partial dependence of features (e.g., first feature)
plot_partial_dependence(rf, X, [0])
plt.show()
