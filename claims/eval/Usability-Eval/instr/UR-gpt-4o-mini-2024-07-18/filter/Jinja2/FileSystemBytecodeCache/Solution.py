from jinja2 import Environment, FileSystemLoader
import os
import hashlib

class BytecodeCache:
    def __init__(self, cache_dir, filename_pattern):
        self.cache_dir = cache_dir
        self.filename_pattern = filename_pattern
        os.makedirs(self.cache_dir, exist_ok=True)

    def _generate_filename(self, key):
        # Create a hash of the key to use in the filename
        key_hash = hashlib.md5(key.encode()).hexdigest()
        return os.path.join(self.cache_dir, self.filename_pattern.format(key_hash=key_hash))

    def get(self, key):
        filename = self._generate_filename(key)
        if os.path.exists(filename):
            with open(filename, 'rb') as f:
                return f.read()
        return None

    def set(self, key, bytecode):
        filename = self._generate_filename(key)
        with open(filename, 'wb') as f:
            f.write(bytecode)

# Example usage
if __name__ == "__main__":
    cache = BytecodeCache('/path/to/cache', 'bytecode_{key_hash}.bin')
    # Save bytecode for a specific key
    cache.set('example_key', b'This is some bytecode.')
    # Retrieve bytecode for the same key
    retrieved_bytecode = cache.get('example_key')
    print(retrieved_bytecode)
