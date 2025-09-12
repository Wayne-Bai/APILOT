
import numpy as np

def scramble_sobol(n, d, scramble_matrix):
    def bit_length(a):
        return a.bit_length()

    def dimension_scramble(u, v):
        mask = np.uint32(1) << bit_length(u) - 1
        while mask:
            u ^= mask * (v & mask)
            v >>= 1
            mask >>= 1
        return u

    W = np.zeros((d, d))

    for i in range(d):
        for j in range(i + 1):
            temp = 1
            u = i + 1
            v = j
            while v:
                if v & 1:
                    temp = dimension_scramble(temp, scramble_matrix[u - 1])
                u = u - 1
                v = v >> 1
            W[i, j] = temp

    def sobol_seq(i, n):
        return (i * 2**np.arange(1, n + 1)) % 2**n

    sobol_seq = np.zeros((d, n))
    for i in range(n):
        for j in range(d):
            sobol_seq[j, i] = sobol_seq(i + 1, bit_length(d))
    
    scrambled_sobol_seq = np.dot(W, sobol_seq) % 1

    return scrambled_sobol_seq
