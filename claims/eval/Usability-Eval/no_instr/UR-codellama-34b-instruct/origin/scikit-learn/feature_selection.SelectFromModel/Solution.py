import pandas as pd
from sklearn.feature_selection import SelectKBest, LinearRegression

# Load the dataset
df = pd.read_csv("your_data.csv")

# Perform feature selection using mutual information
mi = SelectKBest(score_func=lambda X, y: mutual_info_classif(X, y), k=10)
selected_features = mi.fit_transform(df[["feature_a", "feature_b", "feature_c"]], df["target"])

# Create a linear regression model and fit it to the selected features
lr = LinearRegression()
lr.fit(selected_features, df["target"])

# Print the coefficients of the linear regression model
print("Coefficients: \n", lr.coef_)
