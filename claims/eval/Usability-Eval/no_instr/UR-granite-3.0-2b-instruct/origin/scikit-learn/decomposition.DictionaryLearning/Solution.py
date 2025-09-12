import numpy as np
from sklearn.feature_selection import chi2
from sklearn.model_selection import train_test_split

# Assuming X is your data and y are the labels
X = np.random.rand(100, 10)  # Replace this with your data
y = np.random.randint(0, 2, 100)  # Replace this with your labels

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Calculate the chi-squared statistic for each feature
chi2_scores = chi2(X_train, y_train)

# Sort the features by their chi-squared scores
sorted_features = np.argsort(chi2_scores)[::-1]

# Select the top N features (you can choose the number of features you want)
N = 5  # Replace this with the number of features you want
selected_features = sorted_features[:N]

# Print the selected features
print("Selected features:", selected_features)
