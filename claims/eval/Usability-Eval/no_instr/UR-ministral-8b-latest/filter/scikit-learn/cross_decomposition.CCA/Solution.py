import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.cross_decomposition import Ckanova

# Assuming X and Y are your data matrices
X = np.random.randn(100, 5)  # features
Y = np.random.randn(100, 3)  # target

# Create canonical correlation generator
ccja = Ckanova(n_components=2)

# Fit the model
X_cc, Y_cc = ccja.fit_transform(X, Y)

# Display the canonical coordinates
print('Canonical coordinates for X:', X_cc)
print('Canonical coordinates for Y:', Y_cc)
