import time

def z(n, c):
    if n == 0:
        return 0
    else:
        return z(n - 1, c) ** 2 + c

t1 = time.time()
for n in range(25):
    z(n, c=1)
    # print(f"z({n}) = {z(n, c=1)}")
t2 = time.time()

print(f"Time taken: {t2-t1} seconds")

