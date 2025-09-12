from jinja2 import Environment, select_autoescape

class BytecodeCache:
    def __init__(self, directory, pattern):
        self.directory = directory
        self.pattern = pattern
        self.env = Environment(
            autoescape=select_autoescape(['html', 'xml'])
        )
        self.cache_filenames = []

    def _generate_cache_filename(self, bytecode):
        return f"{bytecode}.cache"

    def set_cache_item(self, bytecode):
        filename = self._generate_cache_filename(bytecode)
        filepath = f"{self.directory}/{filename}"
        with open(filepath, 'w') as f:
            f.write(bytecode)
        self.cache_filenames.append(filename)

    def get_cache_item(self, bytecode):
        filename = self._generate_cache_filename(bytecode)
        filepath = f"{self.directory}/{filename}"
        if not filename in self.cache_filenames:
            return None
        with open(filepath, 'r') as f:
            return f.read()

    def remove_cache_item(self, bytecode):
        filename = self._generate_cache_filename(bytecode)
        filepath = f"{self.directory}/{filename}"
        try:
            os.remove(filepath)
            self.cache_filenames.remove(filename)
        except FileNotFoundError:
            pass

# Usage example:
cache = BytecodeCache("cache_directory", "pattern_string")
cache.set_cache_item("example_bytecode")
cached_bytecode = cache.get_cache_item("example_bytecode")
cache.remove_cache_item("example_bytecode")
