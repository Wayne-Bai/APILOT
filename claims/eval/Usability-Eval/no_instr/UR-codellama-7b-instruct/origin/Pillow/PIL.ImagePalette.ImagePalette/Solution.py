
from PIL import Image
import numpy as np

def color_palette(image):
    # Convert image to NumPy array
    image = np.array(image)
    
    # Calculate color palette using K-means clustering
    n_colors = 10
    n_samples = 100
    kmeans = KMeans(n_clusters=n_colors, random_state=0).fit(image)
    centroids = kmeans.cluster_centers_
    colors = centroids[kmeans.labels_]
    
    # Create palette-mapped image
    image_paletted = Image.new('RGB', (100, 100), color=colors)
    
    return image_paletted
