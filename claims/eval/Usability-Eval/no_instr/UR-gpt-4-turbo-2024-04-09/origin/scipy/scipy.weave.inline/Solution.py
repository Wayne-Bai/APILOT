from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize("example.pyx",
                            language_level="3",
                            annotate=True))
