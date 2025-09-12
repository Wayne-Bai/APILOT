import py_compile
import os
import glob

def cache_bytecode(directory, pattern):
    for filepath in glob.glob(os.path.join(directory, pattern)):
        if not filepath.endswith('.pyc'):
            py_compile.compile(filepath)

# call the function passing the directory and pattern as arguments
cache_bytecode('/path/to/directory', '*.py')
