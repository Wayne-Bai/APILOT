from jinja2 import Template
import os
import hashlib

class BytecodeCache:
    def __init__(self, cache_dir, pattern):
        self.cache_dir = cache_dir
        self.pattern = pattern
        
        # Ensure the cache directory exists
        os.makedirs(self.cache_dir, exist_ok=True)

    def _get_cache_file_path(self, *args):
        # Create a unique filename based on the arguments
        filename_template = Template(self.pattern)
        filename = filename_template.render(args=args)
        hashed_filename = hashlib.md5(filename.encode()).hexdigest()
        return os.path.join(self.cache_dir, f"{hashed_filename}.pyc")

    def store(self, args, bytecode):
        cache_file_path = self._get_cache_file_path(*args)
        with open(cache_file_path, 'wb') as f:
            f.write(bytecode)

    def retrieve(self, args):
        cache_file_path = self._get_cache_file_path(*args)
        if os.path.exists(cache_file_path):
            with open(cache_file_path, 'rb') as f:
                return f.read()
        return None
