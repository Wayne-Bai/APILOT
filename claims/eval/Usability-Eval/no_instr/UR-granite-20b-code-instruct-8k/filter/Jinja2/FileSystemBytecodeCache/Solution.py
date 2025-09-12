import jinja2
class BytecodeCache(jinja2.BytecodeCache):
    def __init__(self, directory, pattern):
        self.directory = directory
        self.pattern = pattern

    def load_bytecode(self, key):
        filename = self.pattern.format(key=key)
        bytecode_path = os.path.join(self.directory, filename)
        if os.path.exists(bytecode_path):
            with open(bytecode_path, 'rb') as f:
                return jinja2.Bytecode.from_bytes(f.read())
        else:
            return None

    def dump_bytecode(self, key, bytecode):
        filename = self.pattern.format(key=key)
        bytecode_path = os.path.join(self.directory, filename)
        with open(bytecode_path, 'wb') as f:
            f.write(bytecode.to_bytes())
