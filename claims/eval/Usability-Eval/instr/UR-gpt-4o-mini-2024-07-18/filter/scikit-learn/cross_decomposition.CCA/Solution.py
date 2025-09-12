from sklearn.cross_decomposition import CCA

# Example data
X = [[0.1, 0.2, 0.3], 
     [0.4, 0.5, 0.6], 
     [0.7, 0.8, 0.9]]

Y = [[1.0, 1.1], 
     [1.2, 1.3], 
     [1.4, 1.5]]

# Create a CCA model
cca = CCA(n_components=2)

# Fit the model
cca.fit(X, Y)

# Transform the data
X_c, Y_c = cca.transform(X, Y)

# Output the transformed data
print("Transformed X:", X_c)
print("Transformed Y:", Y_c)
