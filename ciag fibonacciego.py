import numpy as np

def fibo(n):
    if n<2:
        return n

    Q = np.array([[1, 1], [1, 0]])
    W = np.array([[1, 0], [0, 1]])
    n-=1

    while abs(n)>0:
        # print(n)
        if n & 1:   # Sprawdz czy n jest nieparzyste, jesli tak to wykona
            # print(n)
            P = np.matmul(W,Q)
            W = P
            # print('Macierz P:\n',P)
        n >>= 1
        # print('Przesunięcie bitu', n)
        P = np.matmul(Q,Q)
        Q = P
        # print('Macierz P = Q*Q:\n',Q)
    return W[0][0]


n = 2000

print(fibo(n))
