
from sklearn.linear_model import LinearRegression
from sklearn.inspection import plot_partial_dependence
import matplotlib.pyplot as plt

# Load dataset
iris = load_dataset('iris')
X, y = iris.data[:, :2], iris.target

# Create linear regression model
model = LinearRegression()
model.fit(X, y)

# Plot partial dependence plots for first feature
feature1_pd = plot_partial_dependence(model, X, features=[0])
plt.show()
