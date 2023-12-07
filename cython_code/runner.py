import time
from somefunc import somefunc

t1 = time.time()
somefunc(10000000)
t2 = time.time()
print(f"somefunc(10000000) taken: {t2-t1} seconds")

