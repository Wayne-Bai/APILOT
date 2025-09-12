from sklearn.feature_extraction.text import TfidfVectorizer

def compute_density(sparse_vector):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform([sparse_vector])
    density = X.nnz / len(sparse_vector)
    return density
