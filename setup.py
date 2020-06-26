from Cython.Build import cythonize
from setuptools import setup
from setuptools.extension import Extension


setup(
    name='huffman',
    ext_modules=cythonize([
        Extension('huffman', ['huffman.pyx',], language='c++')
    ]),
    zip_safe=False,
)
