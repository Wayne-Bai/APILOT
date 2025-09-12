from sklearn.preprocessing import StandardScaler

# Assuming X_scaled is your scaled data
# Initialize the StandardScaler
scaler = StandardScaler()

# Fit and transform the scaler on your scaled data
X_original = scaler.fit_transform(X_scaled)
