import time
from mandelbrot import z
from somefunc import somefunc

t1 = time.time()
for n in range(25):
    z(n, c=1)
    # print(f"z({n}) = {z(n, c=1)}")
t2 = time.time()
print(f"mandelbrot taken: {t2-t1} seconds")

t1 = time.time()
somefunc(10000000)
t2 = time.time()
print(f"somefunc(10000000) taken: {t2-t1} seconds")

