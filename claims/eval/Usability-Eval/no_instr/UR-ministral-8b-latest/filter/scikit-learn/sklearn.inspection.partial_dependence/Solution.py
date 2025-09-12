import numpy as np
import matplotlib.pyplot as plt
from sklearn.inspection import plot_partial_dependence
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_fitted_house_prices

# Load dataset
X, y = make_fitted_house_prices()

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the model
# Here we would normally import and initialize the estimator, but for this example,
# let's assume we have already trained our estimator `model`
# and would add this section only if required

# Partial Dependence Plot for 'feature1'
features = [0]  # Specify the number of feature for which you want to plot.
plot_partial_dependence(model, X, features, [0])

plt.show()
