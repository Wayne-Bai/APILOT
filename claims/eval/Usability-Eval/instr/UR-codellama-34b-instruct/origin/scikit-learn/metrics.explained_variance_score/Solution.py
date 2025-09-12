
from sklearn.linear_model import LinearRegression

# Create a LinearRegression object and fit it to the data
reg = LinearRegression()
reg.fit(X, y)

# Calculate the explained variance regression score
score = reg.explained_variance_score(X, y)

print("Explained variance regression score:", score)
