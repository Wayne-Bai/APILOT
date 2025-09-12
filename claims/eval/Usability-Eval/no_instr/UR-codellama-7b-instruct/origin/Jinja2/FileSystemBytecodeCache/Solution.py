import os
import glob
from typing import List
from jinja2.environment import Environment
from jinja2.bytecode import Bytecode

class BytecodeCache:
    def __init__(self, directory: str, pattern: str = "*.pyc"):
        self.directory = directory
        self.pattern = pattern
        self.env = Environment()
        
    def get_cache_filenames(self) -> List[str]:
        """Returns a list of cache filenames in the specified directory"""
        return glob.glob(os.path.join(self.directory, self.pattern))
    
    def read_bytecode(self, filename: str) -> Bytecode:
        with open(filename, "rb") as f:
            bytecode = f.read()
        return self.env.parse(bytecode)
        
    def write_bytecode(self, bytecode: Bytecode, filename: str):
        with open(filename, "wb") as f:
            f.write(bytecode.dump())
            
    def clear_cache(self):
        """Clears the cache by deleting all files in the directory"""
        for filename in self.get_cache_filenames():
            os.remove(filename)