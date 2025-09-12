# Import necessary libraries
import pandas as pd  # For data manipulation and analysis
from sklearn.datasets import load_boston  # Load Boston house-prices dataset
from sklearn.model_selection import train_test_split  # For splitting data into training and testing sets

# Load Boston house-prices dataset
boston_dataset = load_boston()

# Convert the dataset to a pandas DataFrame for easier manipulation
data = pd.DataFrame(boston_dataset.data, columns=boston_dataset.feature_names)
data['PRICE'] = boston_dataset.target

# Print the first few rows of the dataset
print(data.head())

# Print the information about the dataset
print(data.info())

# Print the summary statistics of the dataset
print(data.describe())

# Split the dataset into input features (X) and target variable (y)
X = data.drop('PRICE', axis=1)
y = data['PRICE']

# Split the data into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Print the shapes of the training and testing sets
print(f"Training set shape: {X_train.shape}, {y_train.shape}")
print(f"Testing set shape: {X_test.shape}, {y_test.shape}")
