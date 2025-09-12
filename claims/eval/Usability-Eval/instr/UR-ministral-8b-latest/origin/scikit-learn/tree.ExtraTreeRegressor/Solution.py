import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# Preparing random seed
np.random.seed(42)

# Generate dummy data
X, y = np.random.random((500, 10)), np.random.random(500)

# Setting up the model
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Fit the model
model.fit(X, y)

# Making predictions
predictions = model.predict(X)
