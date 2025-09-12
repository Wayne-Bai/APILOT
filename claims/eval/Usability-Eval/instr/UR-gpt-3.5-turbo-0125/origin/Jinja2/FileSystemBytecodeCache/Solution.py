
from jinja2 import Template

template = Template('''
import marshal
import os

class BytecodeCache:
    def __init__(self, cache_dir, pattern):
        self.cache_dir = cache_dir
        self.pattern = pattern

    def store_bytecode(self, code_object, name):
        filename = os.path.join(self.cache_dir, self.pattern.format(name))
        with open(filename, 'wb') as file:
            file.write(marshal.dumps(code_object))

    def load_bytecode(self, name):
        filename = os.path.join(self.cache_dir, self.pattern.format(name))
        if os.path.exists(filename):
            with open(filename, 'rb') as file:
                return marshal.loads(file.read())
        else:
            return None

# Example Usage
cache = BytecodeCache('/path/to/cache', '{{ pattern }}')
code_obj = compile('print("Hello, world!")', '<string>', 'exec')
cache.store_bytecode(code_obj, 'hello_code')

loaded_code_obj = cache.load_bytecode('hello_code')
exec(loaded_code_obj)
''')

pattern = input("Enter pattern string: ")
print(template.render(pattern=pattern))
