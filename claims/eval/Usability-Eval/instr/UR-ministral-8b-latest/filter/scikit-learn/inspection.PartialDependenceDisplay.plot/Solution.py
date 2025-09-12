from sklearn import datasets
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import plot_partial_dependence
import matplotlib.pyplot as plt

# Load dataset
data = datasets.load_boston()
X = data.data
y = data.target

# Initialize the model
model = RandomForestRegressor(n_estimators=50, random_state=42)

# Fit the model
model.fit(X, y)

# Generate and plot partial dependence plots
features = ['RM', 'LSTAT']
plot_partial_dependence(model, X, features, grid_resolution=50)
plt.show()
