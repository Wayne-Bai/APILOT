from sklearn.decomposition import PCA

#假设我们有一个pca模型和初始数据X
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

#要将数据转换回原始空间，我们可以使用inverse_transform函数。
X_original = pca.inverse_transform(X_reduced)
