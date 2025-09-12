
import numpy as np

class AgglomerativeClustering:
    def __init__(self, n_clusters=2, linkage='ward'):
        self.n_clusters = n_clusters
        self.linkage = linkage
        
    def fit_predict(self, X):
        n_samples = X.shape[0]
        self.labels_ = np.zeros(n_samples)
        clusters = [[i] for i in range(n_samples)]
        
        while len(clusters) > self.n_clusters:
            min_distance = np.inf
            merge_idx = None
            
            for i in range(len(clusters)):
                for j in range(i + 1, len(clusters)):
                    distance = self.calculate_distance(X[clusters[i]], X[clusters[j]])
                    if distance < min_distance:
                        min_distance = distance
                        merge_idx = (i, j)
                        
            cluster1, cluster2 = clusters[merge_idx[0]], clusters[merge_idx[1]]
            clusters.append(cluster1 + cluster2)
            del clusters[merge_idx[1]]
            del clusters[merge_idx[0]]
            
        for i, cluster in enumerate(clusters):
            for sample_idx in cluster:
                self.labels_[sample_idx] = i
                
        return self.labels_
    
    def calculate_distance(self, cluster1, cluster2):
        if self.linkage == 'ward':
            return np.linalg.norm(np.mean(cluster1, axis=0) - np.mean(cluster2, axis=0))
