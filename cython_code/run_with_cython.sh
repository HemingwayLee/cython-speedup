# !/bin/bash

cp ../python_code/somefunc.py somefunc.pyx

python3 setup.py build_ext --inplace

