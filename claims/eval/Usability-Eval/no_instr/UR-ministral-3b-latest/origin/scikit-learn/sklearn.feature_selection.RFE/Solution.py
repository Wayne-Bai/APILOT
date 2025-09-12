from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

# Assuming you have already loaded your model and dataset (X, y)
# model = LogisticRegression(max_iter=1000)
# X, y = load_your_dataset_model() # Replace this with the actual code to load the dataset and model

# Initialize the logistic regression model
model = LogisticRegression(max_iter=1000)

# Initialize RFE with the logistic regression model
selector = RFE(model, n_features_to_select=10)  # Specify the number of features to select, change as needed

# Fit the RFE model to the dataset
selector = selector.fit(X, y)  # Replace X and y with your actual dataset

# Extract the ranked features
ranked_features = selector.ranking_  # The ranking of features

# Get the selected features
selected_features = selector.transform(X)  # The selected features
