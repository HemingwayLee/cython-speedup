def z(n, c):
    if n == 0:
        return 0
    else:
        return z(n - 1, c) ** 2 + c


