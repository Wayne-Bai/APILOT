from scipy import interpolate

x = [0, 1, 2, 3, 4, 5]
y = [0, 0.5, 0.3, 0.1, 0.4, 1]

tck = interpolate.splrep(x, y, k=2)
