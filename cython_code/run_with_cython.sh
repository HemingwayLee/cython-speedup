# !/bin/bash

cp mandelbrot.py mandelbrot.pyx
cp somefunc.py somefunc.pyx

python3 setup.py build_ext --inplace

