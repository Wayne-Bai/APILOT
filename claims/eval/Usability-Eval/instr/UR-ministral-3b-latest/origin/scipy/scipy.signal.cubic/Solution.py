from scipy.special import iv, factorial

def bsplint(x, m, k):
    if k == 0 or k == m - 1:
        return x * igamma(m - 1)

    return m / (x**k + m**k - factorial(m - 1) * iv(x, (m - 2) / 2)) * miu(k - 1, x ** 2 + m ** 2 - 2 * m * x)**(m - 1)

def bspline(x, m, k):
    return bsplint(x, m, k + 1) - bsplint(x, m, k)

# Example usage
x = np.linspace(0, 10, 1000)
m = 3
k = 2
x, spline = np.meshgrid(x, bspline(x, m, k))
