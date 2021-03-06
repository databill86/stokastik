import numpy as np

def sieve(n):
    arr = np.empty(n+1, dtype=np.int32)
    arr.fill(1)
    arr[0], arr[1] = 0, 0

    sqrt_n = int(np.sqrt(n))
    for i in range(2, sqrt_n+1):
        if arr[i] == 1:
            j = i**2
            while j <= n:
                arr[j] = 0
                j += i

    return np.nonzero(arr)