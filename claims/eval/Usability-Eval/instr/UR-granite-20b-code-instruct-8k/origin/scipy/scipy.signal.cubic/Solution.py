import scipy.interpolate as spi
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [0, 0.1, 0.5, 0.6, 0.9, 1, 0.9, 0.6, 0.5, 0.1]
tck = spi.splrep(x, y, k=3, s=0)
