import scipy.linalg

# defining a matrix A
A = [
  [1, 2],
  [3, 4],
  [5, 6]
]

# compute the pseudo-inverse matrix of A
A_pinv = scipy.linalg.pinv(A)
A_pinv
