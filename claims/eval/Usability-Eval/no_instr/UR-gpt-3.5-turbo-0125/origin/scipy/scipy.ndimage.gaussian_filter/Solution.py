
import numpy as np

def gaussian_filter(data, sigma):
    kernel = np.fromfunction(lambda x, y: (1/(2*np.pi*sigma**2)) * np.exp(-((x-(data.shape[0]//2))**2 + (y-(data.shape[1]//2))**2)/(2*sigma**2)), data.shape)
    kernel = kernel / np.sum(kernel)
    filtered_data = np.zeros_like(data)
    
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            for k in range(data.shape[2]):
                patch = data[max(0, i-1):min(data.shape[0], i+2), max(0, j-1):min(data.shape[1], j+2), max(0, k-1):min(data.shape[2], k+2)]
                filtered_data[i, j, k] = np.sum(patch * kernel[:patch.shape[0], :patch.shape[1], :patch.shape[2]])
    
    return filtered_data
