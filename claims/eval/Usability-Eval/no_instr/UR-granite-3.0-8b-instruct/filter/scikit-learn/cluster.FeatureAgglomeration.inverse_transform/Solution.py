from sklearn.decomposition import PCA

# Assuming you have a PCA object named 'pca'
# and you want to invert the transformation of a vector 'x'

# Invert the transformation
x_inverted = pca.inverse_transform(x)

# Print the inverted vector
print(x_inverted)
