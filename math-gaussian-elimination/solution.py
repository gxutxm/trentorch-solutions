
import numpy as np


def gaussian_eliminate(A, b):
    """
    Reduce Ax = b to an upper-triangular system Ux = c.
    Assumes no row swaps are needed.
    """
    n = A.shape[0]

    U = A.astype(float).copy()
    c = b.astype(float).copy()

    for i in range(n):
        for j in range(i + 1, n):
            factor = U[j, i] / U[i, i]

            U[j, i:] -= factor * U[i, i:]
            c[j] -= factor * c[i]

    return U, c


def back_substitute(U, c):
    """
    Solve Ux = c from the last row upward.
    """
    n = U.shape[0]
    x = np.zeros(n, dtype=float)

    for i in range(n - 1, -1, -1):
        total = np.sum(U[i, i + 1:] * x[i + 1:])
        x[i] = (c[i] - total) / U[i, i]

    return x
