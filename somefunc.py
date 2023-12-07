import time

def somefunc(K):
    accum = 0
    for i in range(K):
        if i % 5:
            accum = accum + i
    return accum


t1 = time.time()
somefunc(10000000)
t2 = time.time()
print(f"Time taken: {t2-t1} seconds")

