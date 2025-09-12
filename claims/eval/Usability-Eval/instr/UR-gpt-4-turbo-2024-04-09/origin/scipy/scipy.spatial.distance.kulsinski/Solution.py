from scipy.spatial.distance import hamming

u = [0, 1, 0, 1, 1]
v = [1, 0, 1, 1, 0]
result = hamming(u, v)
print("Hamming Distance:", result)
